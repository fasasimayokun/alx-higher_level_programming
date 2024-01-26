#!/usr/bin/python3
"""a Python script that takes 2 arguments in order to solve this challenge.
Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails” You must use the GitHub API,
here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)"""


if __name__ == '__main__':
    import requests
    import sys

    repo = sys.argv[1]
    owner = sys.argv[2]
    nm = 0

    URL = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    resp = requests.get(URL)
    json = resp.json()

    for elem in json:
        if nm > 9:
            break
        sha = elem.get('sha')
        author = elem.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
        nm = nm + 1
