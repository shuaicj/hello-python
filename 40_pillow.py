#!/usr/bin/env python3

# pip3 install pillow

# see https://github.com/python-pillow/Pillow

from PIL import Image

logo = Image.open('github-logo.jpg')
logo.rotate(90).show()
