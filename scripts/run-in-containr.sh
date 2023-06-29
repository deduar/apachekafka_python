#!/bin/bash

(docker network create kafka | true) 2> /dev/null
docker run --network kafka -v $(pwd):/app -w /app --platform linux/amd64 --rm -it python:3.9.4 /bin/bash