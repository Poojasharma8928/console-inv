# Importing library
import qrcode
from PIL import Image
import os,time


def QR(Amount):
# Data to be encoded
    data ="upi://pay?pa=7219624662@upi&pn=Inventory%20Management&tn=yourtext&am={}&cu=INR".format(Amount)

    # Encoding data using make() function
    img = qrcode.make(data)

    # Saving as an image file
    img.save('MyQRCode1.png')
    
    # Read image
    img = Image.open('MyQRCode1.png')
    
    # Output Images
    img.show()
    time.sleep(10)
    os.system('TASKKILL /F /IM Microsoft.Photos.exe')
    img.close()
    os.remove('MyQRCode1.png')
