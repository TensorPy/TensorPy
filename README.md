# TensorPy
[![pypi](https://img.shields.io/pypi/v/tensorpy.svg)](https://pypi.python.org/pypi/tensorpy)

**The fast & easy way to get started with TensorFlow in Python**

TensorPy makes it easier to install and use [TensorFlow](https://www.tensorflow.org/). Use TensorPy to classify multiple images directly from the web without having to download and manage image files manually.


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
python classify.py "https://raw.githubusercontent.com/mdmintz/TensorPy/master/sample_images/happy_animal.jpg"
```

Classify all images on a web page:

```bash
python classify.py "https://github.com/mdmintz/TensorPy/tree/master/sample_images"
```

Classify a single image from a URL from within a Python program: (See [test_classify.py](https://github.com/mdmintz/TensorPy/blob/master/examples/test_classify.py) for details.)

```bash
cd examples
./run_test_classify.sh
```

### ________

For more exciting GitHub projects, such as [SeleniumBase](http://seleniumbase.com), check out [my GitHub page](https://github.com/mdmintz/).
