#!/bin/bash
set -e
# Run example test from inside Docker image
cd /TensorPy/
echo "Running example test: Classify a single image from a URL."
echo "classify https://raw.githubusercontent.com/TensorPy/TensorPy/master/examples/images/happy_animal.jpg"
classify "https://raw.githubusercontent.com/TensorPy/TensorPy/master/examples/images/happy_animal.jpg"
exec "$@"
