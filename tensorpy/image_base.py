import os
import requests
import uuid
from BeautifulSoup import BeautifulSoup
from PIL import Image
from StringIO import StringIO
from tensorpy import classify_image
from tensorpy import constants
from tensorpy import web_core


def get_image_file_dimensions(file_name):
    image = Image.open(file_name)
    image_dimensions = image.size  # (width, height) tuple
    return image_dimensions


def convert_image_file_to_jpg(file_name):
    """ Converts a locally-stored image file to a proper JPEG image file. """
    infile = file_name
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            Image.open(infile).convert('RGBA').save(outfile, "JPEG")
        except IOError:
            raise Exception("Cannot convert %s to jpg!" % file_name)


def load_image_from_url(image_url):
    response = requests.get(image_url)
    image = Image.open(StringIO(response.content)).convert('RGBA')
    return image


def get_image_dimensions(image):
    image_dimensions = image.size
    return image_dimensions


def has_minimum_image_dimensions(image):
    width, height = get_image_dimensions(image)
    if width >= constants.MIN_W_H and height >= constants.MIN_W_H:
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
    soup = BeautifulSoup(completed_source)
    imgs = soup.fetch('img', src=True)
    image_url_list = []
    for img in imgs:
        link = img["src"].split("src=")[-1]
        if (link.endswith('.png') or link.endswith('.jpg')
                or link.endswith('.jpeg')):
            if not link.startswith("http"):
                if ":" not in link:
                    link = full_base_url + link
                else:
                    # The link is weird. Skip it.
                    continue
            image_url_list.append(link)
    return image_url_list


def get_image_classification(image_url):
    downloads_folder = constants.DOWNLOADS_FOLDER
    hex_name = 'temp_image_%s' % uuid.uuid4().get_hex()
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


def classify(image_url):
    """ A shorter method name for get_image_classification() """
    return get_image_classification(image_url)
