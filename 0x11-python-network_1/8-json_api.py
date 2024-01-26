#!/usr/bin/python3
"""a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""


if __name__ == '__main__':
    import requests
    import sys

    URL = 'http://0.0.0.0:5000/search_user'
    data = {'q': sys.argv[1] if len(sys.argv) >= 2 else ""}
    resp = requests.post(URL, data)

    type_resp = resp.headers['content-type']

    if type_resp == 'application/json':
        res = resp.json()
        _id = res.get('id')
        name = res.get('name')
        if (res != {} and _id and name):
            print("[{}] {}".format(_id, name))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
