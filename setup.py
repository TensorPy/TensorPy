"""
The setup package to install TensorPy dependencies.
*> This does NOT include TensorFlow installation.
*> To install TensorFlow, use "./install.sh"
"""

from setuptools import setup, find_packages  # noqa

setup(
    name='tensorpy',
    version='1.1.0',
    url='http://tensorpy.com',
    author='Michael Mintz',
    author_email='mdmintz@gmail.com',
    maintainer='Michael Mintz',
    description='Easy Image Classification with TensorFlow!',
    license='The MIT License',
    install_requires=[
        'requests==2.18.1',
        'six==1.10.0',
        'Pillow==4.1.1',
        'BeautifulSoup4==4.6.0',
    ],
    packages=['tensorpy'],
    entry_points={
        'console_scripts': [
            'classify = tensorpy.classify:main',
        ],
    },
)
