import colorsys
from PIL import Image

# 输入文件
filename = 'test.jpeg'
# 目标色值
target_hue = 0

# 读入图片，转化为 RGB 色值
image = Image.open(filename).convert('RGB')

# 将 RGB 色值分离
image.load()
r, g, b = image.split()
result_r, result_g, result_b = [], [], []
# 依次对每个像素点进行处理
for pixel_r, pixel_g, pixel_b in zip(r.getdata(), g.getdata(), b.getdata()):
    # 转为 HSV 色值
    h, s, v = colorsys.rgb_to_hsv(pixel_r / 255., pixel_b / 255., pixel_g / 255.)
    # 转回 RGB 色系
    rgb = colorsys.hsv_to_rgb(target_hue, s, v)
    pixel_r, pixel_g, pixel_b = [int(x * 255.) for x in rgb]
    # 每个像素点结果保存
    result_r.append(pixel_r)
    result_g.append(pixel_g)
    result_b.append(pixel_b)

r.putdata(result_r)
g.putdata(result_g)
b.putdata(result_b)

# 合并图片
image = Image.merge('RGB', (r, g, b))
# 输出图片
image.save('output.png')