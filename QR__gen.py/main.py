import qrcode as qr
from PIL import Image

'''image = qr.make("https://www.youtube.com/watch?v=OKuiyX5k6zg&t=2190s")
image.save("channel.png")
'''

qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   Box_Size=10,
                   border = 4)
qr.add_data("hello")
qr.make(FIT = True)     #data check kerne ke liye
image = qr.make_image(fill_color = "red", back_color = "blue")
image.save("greeting.png")
