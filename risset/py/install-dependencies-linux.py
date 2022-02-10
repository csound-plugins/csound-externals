#!/usr/bin/env python3

import sys
import os
import re
import subprocess

def get_os():
    output = subprocess.check_output(["hostnamectl"]).decode('utf8')
    for line in output.splitlines():
        line = line.strip()
        if line.startswith('Operating System:'):
            osname = line.split(":", maxsplit=1)[1].strip()
            return osname
    return ""

if not sys.stdin.isatty():
    print("This script should be run from the terminal", file=sys.stderr)
    sys.exit(1)

osname = get_os().lower()


if osname.startswith("ubuntu") or osname.startswith("debian"):
    s = "sudo apt-get -y install python3.9"
elif osname.startswith("fedora"):
    s = "sudo dnf -y install hdf5-devel"
elif osname.startswith("centos"):
    s = "sudo dnf -y install hdf5-devel"
elif osname.startswith("arch"):
    s = "sudo pacman -Syu hdf5"
else:
    print(f"Your operating system / distribution ({osname}) is not "
          "supported", file=sys.stderr)
    sys.exit(1)

print()
print("Installing dependencies for plugin hdf5")
print("=======================================")
print()
print(s)
subprocess.call(s, shell=True)



