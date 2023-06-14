import qrcode

my_qr = qrcode.make("https://www.instagram.com/")
my_qr.save("third_qr.png")
