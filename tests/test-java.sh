#!/bin/bash

# testing compilation of generated java models

rm -rf ../generated/java8
pushd ../
python3 generator.py
popd

cp -f ../build-files/build.gradle ../generated/java8

pushd ../generated/java8 
gradle build
popd
