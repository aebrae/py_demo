#!/usr/bin/env python3
""" Takes previously processed JPEG images from a directory and uploads them to the rest API endpoint"""
import os
import requests

source_path = "/home/supplier_data/images/"
url = "http://www.example.com/upload/"

for file in os.listdir(source_path):
        if file.endswith('jpeg'):
                with open(path, 'rb') as opened:
                        r = requests.post(url, files={'file': opened})
