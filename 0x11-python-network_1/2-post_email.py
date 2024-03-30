#!/usr/bin/python3
""" script that takes in a URL and an email,
    sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
"""
import urllib.parse as parse
import urllib.request as request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    value1 = sys.argv[2]
    value = {'email': value1}
    data = parse.urlencode(value)
    data = data.encode('utf8')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        the_page = response.read()
    print(the_page.decode('utf8'))
