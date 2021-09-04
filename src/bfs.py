import numpy as np
from queue import Queue
from tqdm import tqdm
import cv2
from . import config
from .utils import rgb_to_hex, colour_difference


def get_adjacency_pixels(v, colour):
    res = config.res
    adj = []
    for i in range(-1, 2):
        vx = v[0] + i*res
        if vx >= 0 and vx//res < config.width:
            for j in range(-1, 2):
                vy = v[1] + j*res
                if vy >= 0 and vy//res < config.height:
                    if colour_difference(config.img.getpixel((vx, vy)), colour) > config.threshold:
                        adj.append((vx, vy))

    return adj


# returns relative coords of shape and colour
def bfs(s, visited):
    res, w, h = config.res, config.width, config.height
    sxres, syres = s[0]//res, s[1]//res
    colour = config.img.getpixel(s)
    avgcolour = [colour[0], colour[1], colour[2]]
    colourcount = 1
    d = np.zeros((h+1, w+1), dtype=np.uint8)

    d[syres, sxres] = 255
    visited[syres, sxres] = True

    q = Queue()
    q.put(s)
    while not q.empty():
        u = q.get()

        ucol = config.img.getpixel(u)
        for i in range(3):
            avgcolour[i] += ucol[i]
        colourcount += 1

        adj = get_adjacency_pixels(u, colour)
        for v in adj:
            vxres, vyres = v[0]//res, v[1]//res

            if not visited[vyres, vxres] and d[vyres, vxres] < 255:
                d[vyres, vxres] = 255
                visited[vyres, vxres] = True

                q.put(v)

            # gets rid of pixel 'gaps'
            d[vyres+1, vxres] = 100
            d[vyres, vxres+1] = 100
            d[vyres+1, vxres+1] = 100

    # Finding Contours
    contours, _ = cv2.findContours(
        d, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # cv2.drawContours(d, contours, -1, (0, 0, 255), 3)
    # cv2.imshow('Contours', d)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    for contour in contours:
        lst = contour.tolist()
        vertices = []
        if len(lst) > 2:
            for vertex in lst:
                vertices.append(
                    ("%.4f" % (100 * vertex[0][0]/w), "%.4f" % (100 * vertex[0][1]/h)))
        else:
            return False, None

    for j in range(3):
        avgcolour[j] //= colourcount

    return vertices, rgb_to_hex(tuple(avgcolour))


def convert_bfs():
    print("This can take a while.\nFeel free to go away, watch a film, have a bath, read a book, go on holiday, visit the Gaza Strip, lie to your country about weapons of mass destruction and send troops to Iraq, starting an 8-year-long war and causing civil unrest leading to the insurgence of rebel and terrorist groups like Al-Qaeda and ISIS.")
    res, w, h = config.res, config.width, config.height
    html = f"""<!DOCTYPE html>
<html>
    <head>
        <title>{config.filename}</title>
        <link href="{config.filename}.css" rel="stylesheet" type="text/css">
    </head>
    <body>
"""
    css = f"comp {{width: {50 if w >= h else '%.4f' % ((w/h) * 50)}vw; height: {'%.4f' % ((h/w) * 50) if w >= h else 50}vw; position: absolute;}}"
    count = 0
    visited = np.zeros((h, w), dtype=bool)
    for y in tqdm(range(h)):
        for x in range(w):
            #print(x, y)
            if not visited[y, x]:
                vertices, colour = bfs((x*res, y*res), visited)
                if vertices:
                    count += 1
                    html += f'<comp class="comp-{count}"></comp>'
                    css += f".comp-{count}{{clip-path:polygon("
                    for vertex in vertices:
                        css += f"{vertex[0]}% {vertex[1]}%,"
                    # remove final ','
                    css = css[:-1]
                    css += f");background-color:{colour};}}"
    html += """
    </body>
</html>"""

    return html, css
