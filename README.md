# TensorPy

**The fast & easy way to get started with TensorFlow in Python**

TensorPy simplifies both the installation and usage of TensorFlow so that you can get started with machine learning projects right away. TensorPy comes with a Python library that allows you to classify images directly from the web so that you don't have to worry about downloading and managing image files. There's even a built-in library to locate all images on a web page and classify them together.


### Part I: Setup Instructions for Mac and Ubuntu/Linux

(**Windows & Docker users**: See the [Docker ReadMe](https://github.com/mdmintz/TensorPy/blob/master/docker/ReadMe.md) for running on a Docker machine. Windows requires Docker to run TensorFlow.)

#### **Step 1:** Create/activate a virtual environment named ``tensorpy``

If you're not sure how to create a virtual environment, **[follow these instructions](https://github.com/mdmintz/TensorPy/blob/master/help_docs/virtualenv_instructions.md)** to learn how.

#### **Step 2:** Clone the TensorPy repo from GitHub

```bash
git clone https://github.com/mdmintz/TensorPy.git
cd TensorPy
```

#### **Step 3:** Install TensorFlow and dependancies

It's now just one line of code (see [install_tensorflow.sh](https://github.com/mdmintz/TensorPy/blob/master/install_tensorflow.sh)) to install TensorFlow on your Mac or Linux machine, with all required dependancies, which includes the Imagenet database for classifying images using machine learning.

```bash
./install_tensorflow.sh
```

#### **Step 4:** Install TensorPy

```bash
python setup.py install
```

#### **Step 5:** Run the examples

Classify a single image from a URL, example:

```bash
python classify.py http://theonlinezoo.com/img/04/toz04142l.jpg
```

Classify all images on a web page, example:

```bash
python classify.py http://www.theonlinezoo.com/pages/themes_south_american_animals.html
```

Classifying an image from a URL from within a Python program. See [test_classify.py](https://github.com/mdmintz/TensorPy/blob/master/examples/test_classify.py) to see the code.

```bash
cd examples
./run_test_classify.sh
```

### ________

To see other exciting GitHub projects, check out [my GitHub page](https://github.com/mdmintz/).
