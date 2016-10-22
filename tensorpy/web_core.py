import os
import re
import requests
from tensorpy import settings


def is_valid_url(url):
    regex = re.compile(
        r'^(?:http)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+'
        r'(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if regex.match(url):
        return True
    else:
        return False


def rebuild_source(source, full_base_url):
    """ Completes the links on a web page. """
    source = source.replace('src="//', 'src="http://')
    source = source.replace('src="/', 'src="%s' % full_base_url)
    source = source.replace('src="../', 'src="%s' % full_base_url)
    source = source.replace('src="./', 'src="%s' % full_base_url)
    source = source.replace("src='//", "src='http://")
    source = source.replace("src='/", "src='%s" % full_base_url)
    source = source.replace("src='../", "src='%s" % full_base_url)
    source = source.replace("src='./", "src='%s" % full_base_url)
    return source


def get_content_type(url):
    content = requests.get(url)
    content_type = content.headers['Content-Type']
    if 'html' in content_type:
        return 'html'
    elif 'image/jpeg' in content_type or 'image/png' in content_type:
        return 'image'
    else:
        return 'other'


def download_file(file_url, destination_folder=None):
    """ Downloads the file from the url to the destination folder.
        If no destination folder is specified, the default one is used. """
    if not destination_folder:
        destination_folder = settings.DOWNLOADS_FOLDER
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
    _download_file_to(file_url, destination_folder)


def save_file_as(file_url, new_file_name, destination_folder=None):
    """ Similar to self.download_file(), except that you get to rename the
        file being downloaded to whatever you want. """
    if not destination_folder:
        destination_folder = settings.DOWNLOADS_FOLDER
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
    _download_file_to(
        file_url, destination_folder, new_file_name)


def _download_file_to(file_url, destination_folder, new_file_name=None):
    if new_file_name:
        file_name = new_file_name
    else:
        file_name = file_url.split('/')[-1]
    r = requests.get(file_url)
    with open(destination_folder + '/' + file_name, "wb") as code:
        code.write(r.content)
