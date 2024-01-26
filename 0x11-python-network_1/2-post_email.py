#!/usr/bin/python3
"""a Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body of
the response (decoded in utf-8)"""


if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    email = sys.argv[2]
    dat = urllib.parse.urlencode({"email": email})
    DATA = dat.encode('ascii')

    with urllib.request.urlopen(url, DATA) as response:
        print(response.read().decode('utf-8'))
