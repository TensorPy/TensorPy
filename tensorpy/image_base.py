import os
import requests
import shutil
import sys
import uuid
from bs4 import BeautifulSoup
from io import StringIO
from os import listdir
from os.path import isdir, isfile, join
from PIL import Image
from tensorpy import classify_image
from tensorpy import settings
from tensorpy import web_core


def get_image_file_dimensions(file_name):
    with Image.open(file_name) as image:
        image_dimensions = image.size  # (width, height) tuple
        return image_dimensions


def convert_image_file_to_jpg(file_name):
    """ Converts a locally-stored image file to a proper JPEG image file. """
    infile = file_name
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as image:
                image.convert('RGB').save(outfile, "JPEG")
        except IOError:
            raise Exception("Cannot convert %s to jpg!" % file_name)


def load_image_from_url(image_url):
    response = requests.get(image_url)
    with Image.open(StringIO(response.content)) as image:
        image.convert('RGB')
        return image


def get_image_dimensions(image):
    image_dimensions = image.size
    return image_dimensions


def has_minimum_image_dimensions(image):
    width, height = get_image_dimensions(image)
    if width >= settings.MIN_W_H and height >= settings.MIN_W_H:
        return True
    else:
        return False


def save_image_as_jpg(image, outfile_path):
    image.save(outfile_path, "JPEG")


def get_all_images_on_page(page_url):
    prefix = page_url.split('://')[0]
    simple_url = page_url.split('://')[1]
    base_url = simple_url.split('/')[0]
    full_base_url = prefix + "://" + base_url + "/"
    html = requests.get(page_url)
    completed_source = web_core.rebuild_source(html.text, full_base_url)
    soup = BeautifulSoup(completed_source, "html.parser")
    imgs = soup.find_all("img")
    image_url_list = []
    for img in imgs:
        if not img.has_attr("src") or img.has_attr("onload"):
            continue
        link = img["src"].split("src=")[-1]
        compact_link = link.split('?')[0]
        if (compact_link.endswith('.png') or compact_link.endswith('.jpg') or
                compact_link.endswith('.jpeg')):
            if not link.startswith("http"):
                if ":" not in link:
                    link = full_base_url + link
                else:
                    # The link is weird. Skip it.
                    continue
            image_url_list.append(link)
    return image_url_list


def classify_image_url(image_url):
    """ Classify an image from a URL. """
    downloads_folder = settings.DOWNLOADS_FOLDER
    hex_name = 'temp_image_%s' % uuid.uuid4().hex
    hex_name_png = hex_name + '.png'
    hex_name_jpg = hex_name + '.jpg'
    web_core.save_file_as(image_url, hex_name_png)
    convert_image_file_to_jpg(
        "%s/%s" % (downloads_folder, hex_name_png))
    os.rename(downloads_folder + "/" + hex_name_png,
              downloads_folder + "/temp_image_png.png")
    best_guess = classify_image.external_run(
            "%s/%s" % (downloads_folder, hex_name_jpg))
    os.rename(downloads_folder + "/" + hex_name_jpg,
              downloads_folder + "/temp_image_jpg.jpg")
    return best_guess.strip()


def get_image_classification(image_url):
    # Keep original method name for backwards-compatibility
    return classify_image_url(image_url)


def classify_local_image(file_path):
    """ Classify an image from a local file path. """
    if not file_path.endswith('.jpg') and not file_path.endswith('.png'):
        raise Exception("Expecting a .jpg or .png file!")
    downloads_folder = settings.DOWNLOADS_FOLDER
    hex_name = 'temp_image_%s' % uuid.uuid4().hex
    hex_name_png = hex_name + '.png'
    hex_name_jpg = hex_name + '.jpg'
    shutil.copy2(file_path, os.path.join(downloads_folder, hex_name_png))
    convert_image_file_to_jpg(
        "%s/%s" % (downloads_folder, hex_name_png))
    os.rename(downloads_folder + "/" + hex_name_png,
              downloads_folder + "/temp_image_png.png")
    best_guess = classify_image.external_run(
            "%s/%s" % (downloads_folder, hex_name_jpg))
    os.rename(downloads_folder + "/" + hex_name_jpg,
              downloads_folder + "/temp_image_jpg.jpg")
    return best_guess


def classify_folder_images(folder_path, return_dict=False):
    """ Classify all images from a local folder. """
    classified_images_list = []
    classified_images_dict = {}
    files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    images = [f for f in files if (f.endswith('.jpg') or f.endswith('.png'))]
    total = len(images)
    counter = 0
    for image in images:
        counter += 1
        sys.stdout.write("\rClassifying Image %d of %s..." % (counter, total))
        sys.stdout.flush()
        result = classify_local_image(os.path.join(folder_path, image))
        classified_images_list.append(result)
        classified_images_dict[image] = result
    sys.stdout.write("\rAll classifications have been completed!\n")
    if return_dict:
        return classified_images_dict
    return classified_images_list


def classify(image_url_or_path):
    """ Classify an image from a URL or local file path.
        If a local folder is provided, all images in the folder
        will be classified. """
    is_valid_url = web_core.is_valid_url(image_url_or_path)
    if is_valid_url:
        return classify_image_url(image_url_or_path)
    elif isfile(image_url_or_path):
        return classify_local_image(image_url_or_path)
    elif isdir(image_url_or_path):
        return classify_folder_images(image_url_or_path, return_dict=True)
    else:
        raise Exception("Expecting an image URL, file path, or folder path!")
