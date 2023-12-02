#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')\
            as response:
        html = response.read()
        print("- type: {}".format(type(html)))
        print("- content: {}".format(html))
        print("- utf8 content: {}".format(html.decode('utf-8')))
