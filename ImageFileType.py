# pip install Pillow

import os, sys
from PIL import Image

# Make sure the image you want to change is in the root directory
images = ['test.png'] # add directory in here

for inImage in images:
    f, e = os.path.splitext(inImage)
    outImage = f + '.jpg'
    if inImage != outImage:
        try:
            with Image.open(inImage) as image:
                in_rgb = image.convert('RGB')
                in_rgb.save(outImage, 'JPEG') # converts image
        except OSError:
            print('Conversion failed for', inImage)