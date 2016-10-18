# TensorPy Docker Image
FROM ubuntu:15.10

#=======================================
# Install Python and Basic Python Tools
#=======================================
RUN apt-get update && apt-get install -y python python-pip python-setuptools \
    python-dev python-distribute python-virtualenv

#=========================================
# Install Bash Command Line Tools and Git
#=========================================
RUN apt-get -qy --no-install-recommends install \
    sudo \
    unzip \
    wget \
    curl \
    vim \
    git-core \
  && rm -rf /var/lib/apt/lists/*

#========================================
# Add normal user with passwordless sudo
#========================================
RUN sudo useradd seluser --shell /bin/bash --create-home \
  && sudo usermod -a -G sudo seluser \
  && echo 'ALL ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers

#==============================
# Locale and encoding settings
#==============================
ENV LANGUAGE en_US.UTF-8
ENV LANG ${LANGUAGE}
RUN locale-gen ${LANGUAGE} \
  && dpkg-reconfigure --frontend noninteractive locales 

#==============================
# Set up TensorFlow / TensorPy
#==============================
COPY docker/docker_install.sh /TensorPy/docker_install.sh
COPY download_imagenet.py /TensorPy/download_imagenet.py
COPY classify.py /TensorPy/classify.py
COPY requirements.txt /TensorPy/
COPY setup.py /TensorPy/
COPY tensorpy /TensorPy/tensorpy/
COPY examples /TensorPy/examples/
COPY sample_images /TensorPy/sample_images/
COPY test_classify_image.sh /TensorPy/
COPY docker /TensorPy/docker/
COPY docker/run_docker_test.sh /TensorPy/
RUN cd /TensorPy && ls && ./docker/docker_install.sh
RUN cd /TensorPy && pip install -r requirements.txt

#===================
# Create entrypoint 
#===================
COPY docker/docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/bin/bash"]
