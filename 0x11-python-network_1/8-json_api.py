#!/usr/bin/python3
""" script that takes in a letter
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys
if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    payload = {'q': letter}
    response = requests.post(url, data=payload)
    try:
        json_data = response.json()
        if json_data:
            user_id = json_data.get("id")
            user_name = json_data.get("name")
            print(f"[{user_id}] {user_name}")
        else:
            print("no result")
    except ValueError:
        print("Not valid JSON")
