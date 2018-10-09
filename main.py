import qrcode
import time



data=input("请输入")
img=qrcode.make(data)
img.save("qrcode.jpg")
img.show()