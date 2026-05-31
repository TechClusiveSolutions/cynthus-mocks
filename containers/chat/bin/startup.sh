#!/bin/bash

set -e

server=0.0.0.0
port=${PORT:-5000}

exec /opt/python/bin/uvicorn chat:app --host "${server}" --port "${port}" --reload
