![](http://cdn2.hubspot.net/hubfs/100006/images/tensorpy_logo_4_p.png "TensorPy")
# TensorPy

[![pypi](https://img.shields.io/pypi/v/tensorpy.svg)](https://pypi.python.org/pypi/tensorpy) [![Python version](https://img.shields.io/badge/python-2.7,_3.*-22AADD.svg "Python version")](https://docs.python.org/2/) [![Join the chat at https://gitter.im/TensorPy/Lobby](https://badges.gitter.im/TensorPy/TensorPy.svg)](https://gitter.im/TensorPy/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

**Easy Image Classification with TensorFlow**

[![TensorPy Tutorial](http://img.youtube.com/vi/lVtzaHcUE7Q/3.jpg)](https://www.youtube.com/watch?v=lVtzaHcUE7Q "TensorPy Tutorial")

(**[Watch the 2-minute tutorial on YouTube](https://www.youtube.com/watch?v=lVtzaHcUE7Q)**)

(**Upgraded** since that video was released!)

You can use TensorPy to classify images by simply passing a URL on the command line, or by using TensorPy in your Python programs. **[TensorFlow](https://www.tensorflow.org/)** does all the real work. TensorPy also simplifies TensorFlow installation by automating several setup steps into a single script (See **[install.sh](https://github.com/TensorPy/TensorPy/blob/master/install.sh)** for details).

(Read **[how_tensorpy_works](https://github.com/TensorPy/TensorPy/blob/master/help_docs/how_tensorpy_works.md)** for a detailed explanation of how TensorPy works.)


## Setup Steps for Mac & Ubuntu/Linux

(**Windows & Docker users**: See the **[Docker ReadMe](https://github.com/TensorPy/TensorPy/blob/master/integrations/docker/ReadMe.md)** for running on a Docker machine. Windows requires Docker to run TensorFlow.)

#### **Step 1:** Create and activate a virtual environment named "tensorpy"

If you're not sure how to create a virtual environment, **[follow these instructions](https://github.com/TensorPy/TensorPy/blob/master/help_docs/virtualenv_instructions.md)** to learn how.

#### **Step 2:** Clone the TensorPy repo from GitHub

```bash
git clone https://github.com/TensorPy/TensorPy.git
cd TensorPy
```

#### **Step 3:** Install TensorPy, TensorFlow, and ImageNet/Inception

Use **[install.sh](https://github.com/TensorPy/TensorPy/blob/master/install.sh)** to install everything you need.

```bash
./install.sh
```

#### **Step 4:** Run the examples

(NOTE: Run times may vary depending on your Internet connection and computer's CPU speed.)

Classify a single image from a URL:

```bash
classify "http://cdn2.hubspot.net/hubfs/100006/happy_animal.jpg"
```

Classify all images on a web page:

```bash
classify "https://github.com/TensorPy/TensorPy/tree/master/examples/images"
```

Classify a single image URL from a Python script: (See **[test_python_classify.py](https://github.com/TensorPy/TensorPy/blob/master/examples/test_python_classify.py)** for details.)

```bash
python examples/test_python_classify.py
```

Classify an image from a local file path:

```bash
classify examples/images/cat_animal.jpg
```

Classify all images from a local folder:

```bash
classify examples/images/
```

#### **Examples in Python programs:**

Classify an image from a local file path using a Python script: (See **[test_python_file_classify.py](https://github.com/TensorPy/TensorPy/blob/master/examples/test_python_file_classify.py)** for details.)

```bash
cd examples
python test_python_file_classify.py
```

Classify all images in a local folder using a Python script (Output = LIST): (See **[test_python_folder_classify.py](https://github.com/TensorPy/TensorPy/blob/master/examples/test_python_folder_classify.py)** for details.)

```bash
cd examples
python test_python_folder_classify.py
```

Classify all images in a local folder using a Python script (Output = DICTIONARY): (See **[test_python_folder_classify_dict.py](https://github.com/TensorPy/TensorPy/blob/master/examples/test_python_folder_classify_dict.py)** for details.)

```bash
cd examples
python test_python_folder_classify_dict.py
```

____________

### Future Work:

Eventually, the headline will change from "Image Classification with TensorFlow made easy!" to "Machine Learning with TensorFlow made easy!" once I expand on TensorPy to make other features of TensorFlow easier too. Stay tuned for updates!
