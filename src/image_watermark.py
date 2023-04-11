import os
from PIL import Image


def add_watermark(watermark_path, image_path, out_path, zoom=3, pos=5, offset_x=100, offset_y=100, transparency=0):
    # im是图像，watermark是图片水印
    im = Image.open(image_path).convert('RGBA')
    watermark = Image.open(watermark_path).convert('RGBA')
    # 获取图像的宽高
    w, h = im.size
    # 缩放水印文件
    # zoom = 3
    watermark.thumbnail((w // zoom, h // zoom))
    # 将图像分割成单独的波段
    r, g, b, a = watermark.split()
    # 水印图片尺寸
    w2, h2 = watermark.size

    if pos == 1:
        # 水印的坐标居中
        x = 0
        y = 0
    elif pos == 2:
        # 水印的坐标居中
        x = (w - w2) // 2
        y = 0
    elif pos == 3:
        # 水印的坐标居中
        x = (w - w2)
        y = 0
    elif pos == 4:
        # 水印的坐标居中
        x = 0
        y = (h - h2) // 2
    elif pos == 5:
        # 水印的坐标居中
        x = (w - w2) // 2
        y = (h - h2) // 2
    elif pos == 6:
        # 水印的坐标居中
        x = (w - w2)
        y = (h - h2) // 2
    elif pos == 7:
        # 水印的坐标居中
        x = 0
        y = (h - h2)
    elif pos == 8:
        # 水印的坐标居中
        x = (w - w2) // 2
        y = (h - h2)
    elif pos == 9:
        # 水印的坐标居中
        x = (w - w2)
        y = (h - h2)

    x = x + offset_x
    y = y + offset_y
    # print("x:" + x)
    # print("y:" + y)
    # 法将图片水印给粘贴到图像
    im.paste(watermark, (x, y), mask=a)
    print(out_path)
    out_dir = os.path.dirname(out_path)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    im.save(out_path)


# im.show()


if __name__ == '__main__':
    add_watermark('D:/temp/watermark/logo_gray.png', 'D:/temp/image/0411/1.jpg', 'D:/temp/output/0411/1-1.png', 3, 1,
                  200, 200, 0)
    add_watermark('D:/temp/watermark/logo_gray.png', 'D:/temp/image/0411/1.jpg', 'D:/temp/output/0411/1-5.png', 3, 5, 0,
                  0, 0)
    add_watermark('D:/temp/watermark/logo_gray.png', 'D:/temp/image/0411/1.jpg', 'D:/temp/output/0411/1-7.png', 3, 7,
                  200, -200, 0)
