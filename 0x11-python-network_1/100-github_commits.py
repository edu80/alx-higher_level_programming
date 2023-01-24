#!/usr/bin/python3
"""a Python script that takes 2 arguments to solve challenge
"""

from sys import argv
import requests


if __name__ == '__main__':
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        argv[2], argv[1])
    req = requests.get(url)
    result = req.json()
    for line in result[:10]:
        print('{}: {}'.format(line.get('sha'),
                              line.get('commit').get('author').get('name')))
