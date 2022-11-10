import qrcode
import image 
qr=qrcode.QRCode(version=8,box_size=4,border=2)
data="https://github.com/Vuttalamanish"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("qr.png")
