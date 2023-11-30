#!/bin/bash
# Script that sends a GET request to the passed URL with an additional header
curl -s -H "X-School-User-Id: 98" $1
