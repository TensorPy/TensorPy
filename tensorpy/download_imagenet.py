""" Downloading the ImageNet Inception database. """
# This file is based on:
# https://github.com/tensorflow/models/blob/master/tutorials/image/imagenet/classify_image.py  # noqa

import os
import sys
import tarfile
from six.moves import urllib
from tensorpy import settings
import tensorflow as tf

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string(
    'model_dir', settings.IMAGENET_FOLDER,
    """Path to classify_image_graph_def.pb, """
    """imagenet_synset_to_human_label_map.txt, and """
    """imagenet_2012_challenge_label_map_proto.pbtxt.""")
DATA_URL = ('http://download.tensorflow.org/models/'
            'image/imagenet/inception-2015-12-05.tgz')


def maybe_download_and_extract():
    """Download and extract model tar file."""
    dest_directory = FLAGS.model_dir
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)
    filename = DATA_URL.split('/')[-1]
    filepath = os.path.join(dest_directory, filename)
    if not os.path.exists(filepath):
        def _progress(count, block_size, total_size):
            sys.stdout.write('\r>> Downloading %s %.1f%%' % (
                filename,
                float(count * block_size) / float(total_size) * 100.0))
            sys.stdout.flush()
        filepath, _ = urllib.request.urlretrieve(DATA_URL, filepath, _progress)
        print()
        statinfo = os.stat(filepath)
        print('Succesfully downloaded', filename, statinfo.st_size, 'bytes.')
    tarfile.open(filepath, 'r:gz').extractall(dest_directory)


def main(_):
    maybe_download_and_extract()


tf.compat.v1.app.run()
