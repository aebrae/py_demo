#!/usr/bin/env python3
"""iterates through the descriptions directory and converts each text file to JSON format to post to REST API endpoint"""
import os
import requests

source_path = "/home/supplier_data/descriptions/"
url = "http://www.example.com/uploads/text_descriptions"
fruits = {}

for file_name in os.listdir(source_path):
        if file_name.endswith('txt'):
                with open(source_path+file_name, "r") as file:
                        fruits["fruit"] = file.readline().strip()
                        fruits['weight'] = int(file.readline()[:-5])
                        fruits['description'] = file.readline()[:-1]
                        fruits['image_name'] = file_name[:-3] + "jpeg"
                #print (fruits)
                r = requests.post(url, data = fruits)


""" example text file that gets converted to a JSON dictionary:
watermelon
200 lbs
Watermelons have a longer growing period than other melons.
"""

""" example JSON dictionary converted from text file that gets uploaded to a different REST API endpoint:
{"name": "watermelon", "weight": 200, "description": "Watermelons have a longer growing period than other melons.", "image_name": "watermelon.jpeg"}
"""

