#!/bin/bash
#script that sends a request to a URL and displays only the status code of the response.
curl -so /dev/null --write-out %{http_code} "$1"
