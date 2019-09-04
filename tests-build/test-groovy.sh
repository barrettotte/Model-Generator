#!/bin/bash

# testing compilation of generated groovy models

rm -rf ../generated/groovy
pushd ../
python3 generator.py
popd

cp -f ../build-files/build.gradle ../generated/groovy

pushd ../generated/groovy 
gradle build
popd
