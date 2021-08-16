#!/bin/bash

# A script file for Google Colaboratory


# TeX
# apt-get install texlive-latex-extra  &> tex.log
# apt-get install ghostscript &>> tex.log
# apt-get install dvipng &>> tex.log


# logs
rm -rf *.log


# ArViz & PyMC3
pip install arviz &> arviz.log
pip install pymc3==3.11.2 &> logs/pymc3.log
pip install scikit-learn==0.24.2 &> logs/learn.log


# https://linux.die.net/man/1/wget
wget -q https://github.com/plausibilities/fundamentals/raw/develop/fundamentals.zip


# https://linux.die.net/man/1/unzip
rm -rf fundamentals
unzip -u -q fundamentals.zip
rm -rf fundamentals.zip
