import os
import random


def default_imgpath():
    _, _, filenames = next(os.walk('media/'), (None, None, []))
    return os.path.abspath(f"media/{random.choice(filenames)}")


def update_filename():
    # returns name of file (excl extension)
    x = os.path.basename(imgpath)
    return x.split('.')[0]


# default to a random example image in media folder
imgpath = default_imgpath()

img = None

# filename is set in run.py
filename = ""

# default 50000px limit
limit = 50000

res = 1
width = height = 0

bmethod = False

# default 0.95 threshold
threshold = 0.95
