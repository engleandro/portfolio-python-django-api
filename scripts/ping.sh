#!/bin/bash
wget -O- -q "http://localhost:8000/ping/" | grep "pong"
if [[ $? -eq 0 ]]; then
    echo "ping successful"
else
    echo "ping failed"
    exit 1
fi
