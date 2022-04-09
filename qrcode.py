
# Import QRCode from pyqrcode
import os, sys
import pyqrcode
import png
from pyqrcode import QRCode

#Ask User to input 
fileDir = input('Enter the URL')

splitfile = os.path.splitext(fileDir)[0]

# Generate QR code
url = pyqrcode.create(fileDir)

# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = 8)

# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 6)
