from . import config
from .utils import rgb_to_hex


def write_html():
    return f'''<!DOCTYPE html>
<html>

<head>
    <title>{config.filename}</title>
    <link href="{config.filename}.css" rel="stylesheet" type="text/css">
</head>

<body>
    <div id="{config.filename}"></div>
</body>

</html>
'''


def convert_img():
    res, width, height = config.res, config.width, config.height

    css = f"#{config.filename} {{width:0;height:0;box-shadow:"

    for i in range(width):
        ires = i * res
        for j in range(height):
            jres = j * res
            hex = rgb_to_hex(config.img.getpixel((ires, jres)))
            # last line has semicolon
            if i == width - 1 and j == height - 1:
                css += f"{ires}px {jres}px {res}px {res}px {hex};"
            else:
                css += f"{ires}px {jres}px {res}px {res}px {hex},"
    css += "}"

    return css
