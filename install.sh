# Installs TensorPy, TensorFlow, ImageNet, and required dependancies
# (Made for Python 2.7)

pip install --upgrade pip
echo "Installing TensorPy for Python 2.7:"
pip install -r requirements.txt --upgrade
python setup.py develop
value="$(uname)"
if [ $value == "Linux" ]
then
  echo "Initializing TensorFlow setup on a Linux machine..."
  export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.2.1-cp27-none-linux_x86_64.whl
  pip install --ignore-installed --upgrade $TF_BINARY_URL
elif [ $value == "Darwin" ]
then
  echo "Initializing TensorFlow setup on a MAC..."
  export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.2.1-py2-none-any.whl
  pip install --ignore-installed --upgrade $TF_BINARY_URL
else
  echo "Incompatible machine for TensorFlow. Exiting script..."
fi
echo "Downloading ImageNet Inception DB (for classifying images)..."
python tensorpy/download_imagenet.py
exit
