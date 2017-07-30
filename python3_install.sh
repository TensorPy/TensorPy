# Installs TensorPy, TensorFlow, ImageNet, and required dependancies
# (Made for Python 3)

pip3 install --upgrade pip
echo "Installing TensorPy for Python 3:"
pip3 install -r requirements.txt --upgrade
python3 setup.py install
echo "Installing TensorFlow..."
pip3 install --upgrade tensorflow
echo "Downloading ImageNet Inception DB (for classifying images)..."
python3 tensorpy/download_imagenet.py
exit
