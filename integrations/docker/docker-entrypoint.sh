#!/bin/bash
set -e
echo "***** TensorPy Docker Machine *****"
cd /TensorPy
exec "$@"
