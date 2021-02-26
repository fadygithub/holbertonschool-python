#!/bin/bash
# Receives URL -> sends a request to that URL -> Then it will display size of the response body
curl -sI "$1" | grep Content-Length | cut -d' ' -f2
