#!/bin/bash

docker build -t orbital .

docker run -it --rm --privileged -p 5000:5000 orbital
