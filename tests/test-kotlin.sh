#!/bin/bash

# testing compilation of generated kotlin models

rm -rf ../generated/kotlin
pushd ../
python3 generator.py
popd

cp -f ../build-files/kotlin-build.gradle ../generated/kotlin
mv ../generated/kotlin/kotlin-build.gradle ../generated/kotlin/build.gradle

pushd ../generated/kotlin 
#gradle compileKotlin --info
gradle build
popd
