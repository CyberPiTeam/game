#!/usr/bin/env bash
docker build -t cyberpi_start .
docker run -it -p 8000:8000 cyberpi_start 
