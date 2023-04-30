#!/bin/bash

make

docker run -it --rm -p 5000:5000 orbital
