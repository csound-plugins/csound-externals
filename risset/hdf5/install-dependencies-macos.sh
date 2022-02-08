#!/bin/bash

if ! command -v brew &> /dev/null
then
    echo "brew could not be found, can't install dependencies for hdf5 plugin"
    exit 1
fi

brew install hdf5
