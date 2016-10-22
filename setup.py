"""
The setup package to install TensorPy dependencies.
*> This does NOT include TensorFlow installation.
*> To install TensorFlow, use "./install.sh"
"""

from setuptools import setup, find_packages  # noqa

setup(
    name='tensorpy',
    version='1.0.9',
    url='http://tensorpy.com',
    author='Michael Mintz',
    author_email='@mintzworld',
    maintainer='Michael Mintz',
    description='Image Classification with TensorFlow made easy!',
    license='The MIT License',
    install_requires=[
        'requests==2.11.1',
        'six==1.10.0',
        'Pillow==3.4.2',
        'BeautifulSoup==3.2.1',
    ],
    packages=['tensorpy'],
    entry_points={
        'console_scripts': [
            'classify = tensorpy.classify:main',
        ],
    },
)
