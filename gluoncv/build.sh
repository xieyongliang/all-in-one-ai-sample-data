#!/bin/bash

wget http://data.vision.ee.ethz.ch/cvl/food-101.tar.gz
tar xzvf food-101.tar.gz
mv food-101/* .
rm -rf food-101
python3 ../script/prepare.py

