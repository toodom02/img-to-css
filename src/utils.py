from PIL import Image
from . import config


def colour_difference(rgb1, rgb2):
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    r = (255 - abs(r1 - r2)) / 255
    g = (255 - abs(g1 - g2)) / 255
    b = (255 - abs(b1 - b2)) / 255
    return (r + g + b) / 3


def rgb_to_hex(rgb):
    # hex is faster to load in browsers
    r, g, b = rgb
    return f"#{r:02x}{g:02x}{b:02x}"


def get_image():
    return Image.open(config.imgpath).convert('RGB')


def set_res():
    w, h = config.img.size
    res = 1

    if config.limit == 0:
        return res, w, h

    # ensures total pixels never exceeds limit
    while w//res * h//res > config.limit:
        res += 1

    # scales width, height
    width, height = map(lambda x: x // res, (w, h))

    return res, width, height
