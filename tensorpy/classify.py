import os
import sys
import threading
import uuid
from multiprocessing.dummy import Pool as ThreadPool
from os.path import isdir, isfile
from tensorpy import classify_image
from tensorpy import settings
from tensorpy import image_base
from tensorpy import web_core

lock1 = threading.RLock()
lock2 = threading.RLock()
lock3 = threading.RLock()
images_classified = 0


def download_and_classify_image(image_url):
    global images_classified
    if images_classified >= settings.MAX_IMAGES_PER_PAGE:
        return
    downloads_folder = settings.DOWNLOADS_FOLDER

    # Prevent file conflicts by using unique identifiers
    hex_name = 'temp_image_%s' % uuid.uuid4().hex
    hex_name_png = hex_name + '.png'
    hex_name_jpg = hex_name + '.jpg'

    # Save all images as a "png", but then convert them all to "jpg"
    web_core.save_file_as(image_url, hex_name_png)
    image_base.convert_image_file_to_jpg(
        "%s/%s" % (downloads_folder, hex_name_png))

    # "deleting" files without filling up your recycle bin
    lock2.acquire()
    os.rename(downloads_folder + "/" + hex_name_png,
              downloads_folder + "/temp_image_png.png")
    lock2.release()

    # Classify the image if it's larger than the minimum size
    width, height = image_base.get_image_file_dimensions(
        "%s/%s" % (downloads_folder, hex_name_jpg))
    best_guess = None
    if width >= settings.MIN_W_H and height >= settings.MIN_W_H:
        best_guess = classify_image.external_run(
            "%s/%s" % (downloads_folder, hex_name_jpg))
        lock1.acquire()
        if images_classified == 0:
            print("\n*** "
                  "Classifying all eligible page images:"
                  " ***")
        images_classified += 1
        lock1.release()
        best_guess = best_guess.strip()
        print(best_guess)

    # "deleting" files without filling up your recycle bin
    lock3.acquire()
    os.rename(downloads_folder + '/' + hex_name_jpg,
              downloads_folder + "/temp_image_jpg.jpg")
    lock3.release()


def main():
    expected_arg = "[A valid PAGE_URL or IMAGE_URL]"
    num_args = len(sys.argv)
    if num_args < 2 or num_args > 2:
        print("\n* INVALID RUN COMMAND! *  Usage:")
        print("classify %s\n" % expected_arg)
    elif num_args == 2:
        url = sys.argv[1]
        valid_url = web_core.is_valid_url(url)
        if not valid_url:
            file_path = url
            if isfile(file_path):
                best_guess = image_base.classify_local_image(file_path)
            elif isdir(file_path):
                best_guess = image_base.classify_folder_images(
                    file_path, return_dict=True)
            else:
                raise Exception("Error: %s is not a valid image path!" % url)
            print("\n*** Best match classification: ***")
            print(best_guess)
            print("")
            return
        content_type = web_core.get_content_type(url)
        if content_type == 'other':
            raise Exception(
                "Error: %s does not evaluate to %s" % (url, expected_arg))
        elif content_type == 'image':
            best_guess = image_base.classify_image_url(url)
            print("\n*** Best match classification: ***")
            print(best_guess)
            print("")
        elif content_type == 'html':
            global images_classified
            image_list = image_base.get_all_images_on_page(url)

            if 'linux2' not in sys.platform and settings.MAX_THREADS > 1:
                # Multi-threading the work when not using Docker Linux
                pool = ThreadPool(settings.MAX_THREADS)
                pool.map(download_and_classify_image, image_list)
                pool.close()
                pool.join()
            else:
                # Single-threading the image classification work
                min_w_h = settings.MIN_W_H  # Minimum size for classification
                for image in image_list:
                    web_core.save_file_as(image, "temp_image.png")
                    image_base.convert_image_file_to_jpg(
                        "downloads_folder/temp_image.png")
                    width, height = image_base.get_image_file_dimensions(
                        "downloads_folder/temp_image.jpg")
                    if width >= min_w_h and height >= min_w_h:
                        best_guess = classify_image.external_run(
                            "downloads_folder/temp_image.jpg")
                        if images_classified == 0:
                            print("\n*** "
                                  "Best match classifications for page images:"
                                  " ***")
                        images_classified += 1
                        print(best_guess)
                        if images_classified >= settings.MAX_IMAGES_PER_PAGE:
                            break

            if images_classified >= settings.MAX_IMAGES_PER_PAGE:
                print("\n(NOTE: Exceeded page classification limit "
                      "of %d images per URL! Stopping early.)" % (
                        settings.MAX_IMAGES_PER_PAGE))

            if images_classified == 0:
                print("\nCould not find images to classify on the page! "
                      "(Min size = %dx%d pixels)" % (
                        settings.MIN_W_H, settings.MIN_W_H))
            print("")
        else:
            raise Exception(
                "Unexpected content type %s. Fix the code!" % content_type)


if __name__ == "__main__":
    main()
