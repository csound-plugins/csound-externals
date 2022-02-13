#!/bin/bash

if ! command -v brew &> /dev/null
then
    echo "brew could not be found, can't install dependencies for py plugin"
    exit 1
fi

brew install python@3.9
