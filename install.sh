# Installs TensorPy, TensorFlow, ImageNet, and required dependancies

python -m pip install --upgrade pip
echo "Installing TensorPy:"
pip install -r requirements.txt --upgrade
python setup.py develop
value="$(uname)"
if [ $value = "Linux" ]
then
  echo "Initializing TensorFlow setup on a Linux machine..."
  export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.9.0-cp27-none-linux_x86_64.whl
  pip install --ignore-installed --upgrade $TF_BINARY_URL
elif [ $value = "Darwin" ]
then
  echo "Initializing TensorFlow setup on a MAC..."
  pip install --upgrade tensorflow
else
  echo "Incompatible machine for TensorFlow. Exiting script..."
fi
echo "Downloading ImageNet Inception DB (for classifying images)..."
python tensorpy/download_imagenet.py
exit
