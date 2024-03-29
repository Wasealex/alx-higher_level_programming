#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status
"""
import requests
if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print(f"""Body response:\n\t- type: {type(response.text)}
\t- content: {response.text}""")
