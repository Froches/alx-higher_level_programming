#!/bin/bash
# Script that takes in a URL, sends a request to it and displsys the bosy size of the response
curl -s "$1" | wc -c
