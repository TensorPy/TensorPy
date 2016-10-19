#!/bin/bash
set -e
# Run example test from inside Docker image
cd /TensorPy/
echo "Running example test: Classify a single image from a url."
echo "python classify.py https://raw.githubusercontent.com/TensorPy/TensorPy/master/sample_images/happy_animal.jpg"
python classify.py "https://raw.githubusercontent.com/TensorPy/TensorPy/master/sample_images/happy_animal.jpg"
exec "$@"
