#!/bin/bash
set -e
# Run example test from inside Docker image
cd /TensorPy/
echo "Running example one: Classify a single image from a url."
echo "python classify.py http://theonlinezoo.com/img/04/toz04142l.jpg"
python classify.py http://theonlinezoo.com/img/04/toz04142l.jpg
exec "$@"
