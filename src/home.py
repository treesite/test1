import binascii
import base64


def parse2(file):
    return base64.b64encode(file)


img = input("请输入文件地址:")
res = parse2(img)
print(res)

