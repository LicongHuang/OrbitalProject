#!/bin/bash

docker build -t orbital .

docker run -it --rm -p 5000:5000 orbital
