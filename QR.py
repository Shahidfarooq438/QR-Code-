import qrcode

qr=qrcode.QRCode(
    version=10,
    box_size=10,
    border=5
    )

data="https://www.linkedin.com/in/shahid-farooq-540027229/"
qr.add_data(data)
qr.make(fit=True)

img=qr.make_image(fill="black",back_color="white")
img.save('qrcode1.png')