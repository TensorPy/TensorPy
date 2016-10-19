# TensorPy
![](http://cdn2.hubspot.net/hubfs/100006/images/tensorpy_logo_p.png "TensorPy")

[![pypi](https://img.shields.io/pypi/v/tensorpy.svg)](https://pypi.python.org/pypi/tensorpy) [![Python version](https://img.shields.io/badge/python-2.7-22AADD.svg "Python version")](https://docs.python.org/2/) [![MIT License](http://img.shields.io/badge/license-MIT-22BBCC.svg "MIT License")](https://github.com/mdmintz/TensorPy/blob/master/LICENSE)

**Making TensorFlow easier to use with Python**

You can use TensorPy to classify images by simply passing a URL. [TensorFlow](https://www.tensorflow.org/) image recognition does the hard work.


### Setup Instructions for Mac and Ubuntu/Linux

(**Windows & Docker users**: See the [Docker ReadMe](https://github.com/mdmintz/TensorPy/blob/master/docker/ReadMe.md) for running on a Docker machine. Windows requires Docker to run TensorFlow.)

#### **Step 1:** Create and activate a virtual environment named "tensorpy"

If you're not sure how to create a virtual environment, **[follow these instructions](https://github.com/mdmintz/TensorPy/blob/master/help_docs/virtualenv_instructions.md)** to learn how.

#### **Step 2:** Clone the TensorPy repo from GitHub

```bash
git clone https://github.com/mdmintz/TensorPy.git
cd TensorPy
```

#### **Step 3:** Install TensorPy, TensorFlow, and ImageNet

One script installs them all. (See [install.sh](https://github.com/mdmintz/TensorPy/blob/master/install.sh) for details.)

```bash
./install.sh
```

#### **Step 4:** Run the examples

Classify a single image from a URL:

```bash
classify "https://raw.githubusercontent.com/mdmintz/TensorPy/master/sample_images/happy_animal.jpg"
```

Classify all images on a web page:

```bash
classify "https://github.com/mdmintz/TensorPy/tree/master/sample_images"
```

Classify a single image from a URL from within a Python program: (See [test_python_classify.py](https://github.com/mdmintz/TensorPy/blob/master/examples/test_python_classify.py) for details.)

```bash
cd examples
python test_python_classify.py
```
