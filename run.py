from sys import argv
import os
import random
from src.convert import convert_img, get_filename, write_html
from src.write import write_to_css, write_to_HTML


def main():
    if argv[1:]:
        imgfile = argv[1]
    else:
        # default to a random example image
        imgfile = f"media/{random.choice(['example','largexample','monalisa','homer','vangogh'])}.jpg"

    filename = get_filename(imgfile)
    cssString = convert_img(imgfile)
    htmlString = write_html(filename)

    write_to_css(filename, cssString)
    write_to_HTML(filename, htmlString)

    # open htmlfile when finished
    os.startfile(os.path.abspath(f"output/{filename}.html"), 'open')


if __name__ == '__main__':
    main()
