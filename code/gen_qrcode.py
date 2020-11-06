import qrcode
import pandas as pd
import os

data = pd.read_csv("/home/chihq/SX-FS 21.csv")
data = data.dropna(subset=["Designs Artwork"])
path_qrcode = "/home/chihq/Desktop/try_tiff/qrcode_img"
def gen_code(text):
    path = os.path.join(path_qrcode, text+".png")
    qr = qrcode.QRCode(box_size=115)
    qr.add_data(text)
    qr.make()
    img = qr.make_image()
    img.save(path)
for text in data["Stock Moves/Sale Line/Barcode"]:
    print(text)
    gen_code(text)