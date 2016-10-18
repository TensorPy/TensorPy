"""
The setup package to install TensorPy dependencies
*> This does NOT include TensorFlow installation
*> To install TensorFlow, use "./install_tensorflow.sh"
"""

from setuptools import setup, find_packages  # noqa

setup(
    name='tensorpy',
    version='1.0.0',
    url='http://tensorpy.com',
    author='Michael Mintz',
    author_email='@mintzworld',
    maintainer='Michael Mintz',
    description='The fast & easy way to get started with Tensorflow',
    license='The MIT License',
    install_requires=[
        'requests==2.11.1',
        'six>=1.10.0',
        'Pillow==3.4.1',
        'BeautifulSoup==3.2.1',
        ],
    packages=['tensorpy'],
    )
