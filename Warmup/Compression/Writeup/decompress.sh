#!/bin/bash

file flag.txt
mv flag.txt flag.bzip2
bzip2 -d flag.bzip2
mv flag.bzip2.out flag.txt
file flag.txt
mv flag.txt flag.xz
xz -d flag.xz
mv flag flag.txt
file flag.txt
mv flag.txt flag.gz
gzip -d flag.gz
mv flag flag.txt
file flag.txt
mv flag.txt flag.tar
tar xvf flag.tar
cat flag.txt
rm flag.tar
