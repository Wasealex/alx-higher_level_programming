#!/usr/bin/python3
"""script that takes in a URL,
sends a request to the URL and
displays the body of the response (decoded in utf-8)
"""
import urllib.request as request
import urllib.error as error
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            body = response.read().decode('utf8')
        print(body)

    except error.URLError as errors:
        error_code = errors.code
        print(f"Error code: {error_code}")
