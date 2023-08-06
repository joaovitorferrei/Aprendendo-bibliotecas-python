import qrcode

image_qrcode = qrcode.make("https://github.com/joaovitorferrei")
image_qrcode.save("qrcode_python.png")