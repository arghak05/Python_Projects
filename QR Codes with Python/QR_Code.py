import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = input('Enter the url: ')
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the svg file naming 'myqr.svg'
url.svg('G:\PYTHON PROJECTS FOR BEGINNERS\QR Codes with Python\myqr.svg',scale=8)

# Create and save the png file naming 'myqr.png'
url.png('G:\PYTHON PROJECTS FOR BEGINNERS\QR Codes with Python\myqr.png',scale=8)