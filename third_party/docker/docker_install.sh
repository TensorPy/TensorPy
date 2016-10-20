# Installs TensorPy, TensorFlow, ImageNet, and required dependancies
# (Special Docker edition!)

pip install --upgrade pip
echo "Installing TensorPy..."
python setup.py install
echo "Initializing TensorFlow setup on an Ubuntu Docker machine..."
export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.10.0-cp27-none-linux_x86_64.whl
pip install $TF_BINARY_URL
echo "Downloading ImageNet (image database for classifying images)..."
python tensorpy/download_imagenet.py
exit
