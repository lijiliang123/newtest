import requests

'''
url='//mat1.gtimg.com/pingjs/ext2020/2018/js/check-https-content.js'
res=requests.get(url)
res.encoding='UTF-8'
con=res.text
print(con)
'''

from PIL import Image, ImageDraw, ImageFont
import os

for i in range(1, 3):
    # 创建图像,设置图像大小及颜色
    im = Image.new('RGBA', (1000, 1800), (166, 12, 4, 255))
    draw = ImageDraw.Draw(im)
    # 设置本次使用的字体
    fontsFolder = 'C:WindowsFonts'
    font1 = ImageFont.truetype(os.path.join(fontsFolder, '华康俪金黑W8.TTF'), 420)
    font2 = ImageFont.truetype(os.path.join(fontsFolder, '方正兰亭刊黑.TTF'), 40)
    # 计算各文本的放置位置
    txtSize_1 = draw.textsize('距 离 除 夕 夜', font2)
    pos_x_1 = (1000 - txtSize_1[0]) / 2
    txtSize_2 = draw.textsize('还 有', font2)
    pos_x_2 = (1000 - txtSize_2[0]) / 2
    txtSize_3 = draw.textsize('天', font2)
    pos_x_3 = (1000 - txtSize_3[0]) / 2
    txtSize_4 = draw.textsize('不 是 年 味 越 来 越 少', font2)
    pos_x_4 = (1000 - txtSize_4[0]) / 2
    txtSize_5 = draw.textsize('而 是 我 们 都 长 大 了', font2)
    pos_x_5 = (1000 - txtSize_5[0]) / 2
    # 设置文本放置位置,居中
    draw.text((pos_x_1, 200), '距 离 除 夕 夜', fill=(217, 217, 217, 255), font=font2)
    draw.text((pos_x_2, 300), '还 有', fill=(217, 217, 217, 255), font=font2)
    draw.text((pos_x_3, 1050), '天', fill=(217, 217, 217, 255), font=font2)
    draw.text((pos_x_4, 1350), '不 是 年 味 越 来 越 少', fill=(137, 183, 109, 255), font=font2)
    draw.text((pos_x_5, 1440), '而 是 我 们 都 长 大 了', fill=(137, 183, 109, 255), font=font2)
    # 绘制线框
    draw.line([(20, 20), (980, 20), (980, 1780), (20, 1780), (20, 20)], fill=(217, 217, 217, 255), width=5)
    # 设置变化的文本属性
    txtSize_6 = draw.textsize(str(i), font1)
    pos_x_6 = (1000 - txtSize_6[0]) / 2
    draw.text((pos_x_6, 500), str(i), fill=(137, 183, 109, 255), font=font1)
    # im.show()
    # 保存图像
    filename = 'day' + str(i) + '.png'
    im.save(filename)
