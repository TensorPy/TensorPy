# Installs TensorPy, TensorFlow, ImageNet, and required dependancies

pip install --upgrade pip
python setup.py install
value="$(uname)"
if [ $value == "Linux" ]
then
  echo "Initializing tensorflow setup on a Linux machine..."
  export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.10.0-cp27-none-linux_x86_64.whl
  pip install $TF_BINARY_URL
elif [ $value == "Darwin" ]
then
  echo "Initializing tensorflow setup on a MAC..."
  export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.10.0-py2-none-any.whl
  pip install $TF_BINARY_URL
else
  echo "Incompatible machine for Tensorflow. Exiting script..."
fi
echo "Downloading ImageNet (image recognition library)..."
python download_imagenet.py
exit
