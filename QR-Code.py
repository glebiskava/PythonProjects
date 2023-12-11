import qrcode

I = input("Type in the URL which you want to visit: ")

print("The QRCode is now saved: ", I)

def generate(data, img_name="qrCode.png"):
    img = qrcode.make(data)
    img.save(img_name)
    return

generate(I)