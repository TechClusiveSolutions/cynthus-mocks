#!/bin/bash

set -e

server=0.0.0.0
port=$PORT

if (( -v port )); then
    port=8000
fi

exec /opt/python/bin/uvicorn api:app --host "$server" --port "$port" --reload
