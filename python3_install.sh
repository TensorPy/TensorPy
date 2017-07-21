# Installs TensorPy, TensorFlow, ImageNet, and required dependancies
# (Made for Python 3)

pip3 install --upgrade pip
echo "Installing TensorPy for Python 3:"
pip3 install -r requirements.txt --upgrade
python3 setup.py install
value="$(uname)"
if [ $value == "Linux" ]
then
  echo "Initializing TensorFlow setup on a Linux machine..."
  pip3 install --upgrade tensorflow
elif [ $value == "Darwin" ]
then
  echo "Initializing TensorFlow setup on a MAC..."
  pip3 install --upgrade tensorflow
else
  echo "Incompatible machine for TensorFlow. Exiting script..."
fi
echo "Downloading ImageNet Inception DB (for classifying images)..."
python3 tensorpy/download_imagenet.py
exit
