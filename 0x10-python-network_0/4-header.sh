#!/bin/bash
#script that sends a GET request to the URLand displays the body of the response
curl -sX GET -H "X-School-User-Id:98" "$1"
