# generate a qr code with image in it 
import qrcode
from PIL import Image

my_logo = 'offer.png'

open_logo = Image.open(my_logo)
basewidth = 100
wpercent = (basewidth/float(open_logo.size[0]))
hsize = int((float(open_logo.size[1])*float(wpercent)))
logo = open_logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
wether =  {
     'temperature' : "32 degree",
     'atmosphere' : 'Haze',
     'location':'Bhavnagar'
}

QRcode.add_data(wether)
QRcode.make()
QRimg = QRcode.make_image(
    fill_color="yellow", back_color="red").convert('RGB')
 
# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2,
       (QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)
# save the QR code generated
QRimg.save('logo_qr.png')
print('QR code generated!')

