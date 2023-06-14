import qrcode
qr = qrcode.QRCode()
qr.add_data("Second example ")
qr.make(fit=True)
img = qr.make_image(fill_color="yellow", back_color="black")
img.save("fourth_example.png")