#!/bin/bash

exiftool ../oq7hs.jpg | grep -oE "EPICTF{.*}"
