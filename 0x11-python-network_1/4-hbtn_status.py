#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == '__main__':
    req = requests.get('https://alx-intranet.hbtn.io/status')
    mes = req.text
    print("Body response:")
    print("\t- type: {}".format(type(mes)))
    print("\t- content: {}".format(mes))
