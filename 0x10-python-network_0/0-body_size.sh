#!/bin/bash
# Script that displays the size of the body of the HTTP response
curl -sI $1 | grep Content-Length | cut -d' ' -f2
