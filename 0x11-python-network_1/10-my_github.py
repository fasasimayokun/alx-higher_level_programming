#!/usr/bin/python3
"""a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""


if __name__ == '__main__':
    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]

    URL = "https://api.github.com/user"
    resp = requests.get(URL, auth=(username, password))
    json = resp.json()

    print(json.get('id'))
