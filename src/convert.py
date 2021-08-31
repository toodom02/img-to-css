from PIL import Image
import os


def rgb_to_hex(r, g, b):
    # hex is faster to load in browsers
    return f"#{r:02x}{g:02x}{b:02x}"


def get_filename(filepath):
    # returns name of file (excl extension)
    x = os.path.basename(filepath)
    return x.split('.')[0]


def get_res(img):
    w, h = img.size
    res = 1
    # ensures total pixels never exceeds 50000
    while w//res * h//res > 50000:
        res += 1

    # scales width, height
    width, height = map(lambda x: x // res, (w, h))

    return res, width, height


def write_html(filename):
    return f'''<!DOCTYPE html>
<html>

<head>
    <title>{filename}</title>
    <link href="{filename}.css" rel="stylesheet" type="text/css">
</head>

<body>
    <div id="{filename}" />
</body>

</html>
'''


def convert_img(imgpath):
    img = Image.open(imgpath)
    img = img.convert('RGB')
    res, width, height = get_res(img)
    filename = get_filename(imgpath)

    css = f"#{filename} {{width:0;height:0;box-shadow:"

    for i in range(width):
        ires = i * res
        for j in range(height):
            jres = j * res
            r, g, b = img.getpixel((ires, jres))
            hex = rgb_to_hex(r, g, b)
            # last line has semicolon
            if i == width - 1 and j == height - 1:
                css += f"{ires}px {jres}px {res}px {res}px {hex};"
            else:
                css += f"{ires}px {jres}px {res}px {res}px {hex},"
    css += "}"

    return css
