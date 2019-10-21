from PIL import Image


def parsegif(file,dir):
    myimage=Image.open(file)
    zs = 0
    if myimage:
        while True:
            try:
                myimage.seek(zs)
                zs += 1
            except:
                break

        for i in  range(zs):
            myimage.seek(i)
            myimage.save(dir+"{:02d}.bmp".format(myimage.tell()))
        return zs
    else:
        return False


img = input("请输入gif图片地址:")
res = parsegif(img, "D:/PythonProjects/timg/timg")
# res = parsegif("D:/PythonProjects/timg.gif", "D:/PythonProjects/timg/timg")

if res:
    print("处理结束，共%d帧，各帧已被保存！"%res)
else:
    print("无法打开文件！")

