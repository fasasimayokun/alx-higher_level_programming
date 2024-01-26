#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)."""


if __name__ == '__main__':
    import urllib
    import sys

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.status))
