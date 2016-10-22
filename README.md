# TensorPy
![](http://cdn2.hubspot.net/hubfs/100006/images/tensorpy_logo_4_p.png "TensorPy")

[![pypi](https://img.shields.io/pypi/v/tensorpy.svg)](https://pypi.python.org/pypi/tensorpy) [![GitHub stars](https://img.shields.io/github/stars/TensorPy/TensorPy.svg "GitHub stars")](https://github.com/TensorPy/TensorPy/stargazers) [![Python version](https://img.shields.io/badge/python-2.7-22AADD.svg "Python version")](https://docs.python.org/2/) [![MIT License](http://img.shields.io/badge/license-MIT-22BBCC.svg "MIT License")](https://github.com/TensorPy/TensorPy/blob/master/LICENSE) [![Join the chat at https://gitter.im/TensorPy/Lobby](https://badges.gitter.im/TensorPy/TensorPy.svg)](https://gitter.im/TensorPy/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

**Image Classification with TensorFlow made easy!**

[![TensorPy Tutorial](http://img.youtube.com/vi/lVtzaHcUE7Q/3.jpg)](https://www.youtube.com/watch?v=lVtzaHcUE7Q "TensorPy Tutorial")

(**[The 2-Minute Video Demo](https://www.youtube.com/watch?v=lVtzaHcUE7Q)**)

You can use TensorPy to classify images by simply passing a URL on the command line, or by using TensorPy in your Python programs. **[TensorFlow](https://www.tensorflow.org/)** does all the image-recognition work. TensorPy also simplifies TensorFlow installation by automating several setup steps into a single script (See **[install.sh](https://github.com/TensorPy/TensorPy/blob/master/install.sh)** for details).

(Read **[how_tensorpy_works](https://github.com/TensorPy/TensorPy/blob/master/help_docs/how_tensorpy_works.md)** for a detailed explanation of how TensorPy works.)


## Setup Steps for Mac & Ubuntu/Linux

(**Windows & Docker users**: See the **[Docker ReadMe](https://github.com/TensorPy/TensorPy/blob/master/third_party/docker/ReadMe.md)** for running on a Docker machine. Windows requires Docker to run TensorFlow.)

#### **Step 1:** Create and activate a virtual environment named "tensorpy"

If you're not sure how to create a virtual environment, **[follow these instructions](https://github.com/TensorPy/TensorPy/blob/master/help_docs/virtualenv_instructions.md)** to learn how.

#### **Step 2:** Clone the TensorPy repo from GitHub

```bash
git clone https://github.com/TensorPy/TensorPy.git
cd TensorPy
```

#### **Step 3:** Install TensorPy, TensorFlow, and ImageNet/Inception

The **[install.sh](https://github.com/TensorPy/TensorPy/blob/master/install.sh)** script installs everything you need:

```bash
./install.sh
```

#### **Step 4:** Run the examples

Classify a single image from a URL:

```bash
classify "http://cdn2.hubspot.net/hubfs/100006/happy_animal.jpg"
```

Classify all images on a web page:

```bash
classify "https://github.com/TensorPy/TensorPy/tree/master/examples/images"
```

Classify a single image from a URL from within a Python program: (See **[test_python_classify.py](https://github.com/TensorPy/TensorPy/blob/master/examples/test_python_classify.py)** for details.)

```bash
cd examples
python test_python_classify.py
```

____________

### Future Work:

Eventually, the headline will change from "Image Classification with TensorFlow made easy!" to "Machine Learning with TensorFlow made easy!" once I expand on TensorPy to make other features of TensorFlow easier too. Stay tuned for updates!
