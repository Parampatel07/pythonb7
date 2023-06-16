import qrcode
def make_qr(data,image_name,text_color="black",bg_color="white"):
     qr = qrcode.QRCode()
     qr.add_data(data)
     qr.make(fit=True)
     img = qr.make_image(fill_color=text_color, back_color=bg_color)
     img.save(image_name)

wether =  {
     'temperature' : "32 degree",
     'atmosphere' : 'Haze',
     'location':'Bhavnagar'
}
make_qr(wether,"wether1.png")
make_qr(wether,"wether2.png",text_color="aqua",bg_color="black")

