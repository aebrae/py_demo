#!/usr/bin/env python3
"""Process the new images to the following specs and places them in the same folder: 
        --change resolution from 3000x2000 to 600x400 pixel
        --change image format from .TIFF to .JPEG
"""
import os
from PIL import Image

source_path      = '/home/supplier_data/images/'
destination_path = '/home/supplier_data/images/'

for file in os.listdir(source_path):
        if file.endswith('tiff'):
                im = Image.open(source_path+file)
                #print(destination_path+file[:-4]+"jpeg")
                new_im = im.convert("RGB").resize((600,400)).save(destination_path+file[:-4]+"jpeg",format="jpeg") 
