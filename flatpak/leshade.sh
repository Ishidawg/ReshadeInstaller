#!/bin/bash

export PYTHONPATH=$PYTHONPATH:/app/share/leshade
python3 /app/share/reshade-installer/main.py "$@"
