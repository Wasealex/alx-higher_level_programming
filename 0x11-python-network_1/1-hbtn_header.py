#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
displays the value of the 'X-Request-Id'
variable found in the header of the response.
"""
import sys
import urllib.request as request
if __name__ == '__main__':
    with request.urlopen(request.Request(sys.argv[1])) as response:
        print(response.headers.get('X-Request-Id'))
