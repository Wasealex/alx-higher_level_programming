#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen(
            'https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
    print(
        f"""Body response:
        - type: {type(html)}
        - content: {html}
        - utf8 content: {html.decode('utf8')}""")
