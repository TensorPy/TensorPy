"""
The setup package to install TensorPy dependencies.
*> This does NOT include TensorFlow installation.
*> To install TensorFlow, use "./install.sh"
"""

from setuptools import setup, find_packages  # noqa
from os import path


this_directory = path.abspath(path.dirname(__file__))
long_description = None
try:
    with open(path.join(this_directory, 'README.md'), 'rb') as f:
        long_description = f.read().decode('utf-8')
except IOError:
    long_description = 'Easy Image Classification with TensorFlow!'

setup(
    name='tensorpy',
    version='1.4.2',
    description='Easy Image Classification with TensorFlow!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/TensorPy/TensorPy',
    platforms=["Linux", "Unix", "Mac OS-X"],
    author='Michael Mintz',
    author_email='mdmintz@gmail.com',
    maintainer='Michael Mintz',
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires='>=3.5, <3.8',
    install_requires=[
        'tensorflow==1.15.4',
        'six>=1.11.0',
        'requests>=2.18.4',
        'Pillow==5.4.1',
        'BeautifulSoup4>=4.6.0',
    ],
    packages=['tensorpy'],
    entry_points={
        'console_scripts': [
            'classify = tensorpy.classify:main',
        ],
    },
)
