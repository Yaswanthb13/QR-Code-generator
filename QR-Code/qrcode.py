#import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode 

#String which represents the QR-Code
site="https://www.google.co.in/"

#Generating QR-Code
qr_code=pyqrcode.create(site)

#create and save the svg file naming "qrcode.svg"  
#svg file is just for  having high resolution of the qrcode
qr_code.svg("google.svg",scale=8)

#create and save the png file naming "qrcode.png"
qr_code.png("google.png",scale=6)