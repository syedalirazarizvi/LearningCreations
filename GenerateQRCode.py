# Generating QR Code from user Input
# For this task you need to install module pyqrcode from pip install
# Generated QR Code SVG file will be stored in the same folder where this script exist

import pyqrcode as pq

mc= input("Enter text for Creating QR Code : ")

mycode = pq.create(mc)
mycode.svg("code.svg", scale=5)
print("done...")

input()
