# Installs TensorPy, TensorFlow, ImageNet, and required dependancies
# (Special Docker edition!)

pip install --upgrade pip
python setup.py install
echo "Initializing tensorflow setup on an Ubuntu machine..."
export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.10.0-cp27-none-linux_x86_64.whl
pip install $TF_BINARY_URL
echo "Downloading ImageNet (image recognition library)..."
python download_imagenet.py
exit
