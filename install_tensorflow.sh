# Tensorflow Installation Script
# (Installs Tensorflow and required dependencies)

pip install --upgrade pip
pip install requests==2.11.1
pip install six==1.10.0
pip install Pillow==3.4.1
pip install BeautifulSoup==3.2.1
value="$(uname)"
if [ $value == "Linux" ]
then
  echo "Initializing tensorflow setup on a Linux machine..."
  export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.11.0rc0-cp27-none-linux_x86_64.whl
  pip install $TF_BINARY_URL
elif [ $value == "Darwin" ]
then
  echo "Initializing tensorflow setup on a MAC..."
  export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.11.0rc0-py2-none-any.whl
  pip install $TF_BINARY_URL
else
  echo "Incompatible machine for Tensorflow. Exiting script..."
fi
echo "Downloading ImageNet (image recognition library)..."
python download_imagenet.py
exit
