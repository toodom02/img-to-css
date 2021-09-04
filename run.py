import sys
import os
import getopt
import src.config as config
from src.utils import get_image, set_res
from src.convert import convert_img, write_html
from src.write import write_to_css, write_to_HTML
from src.bfs import convert_bfs


def handle_args():
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "i:l:bt:")
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        sys.exit(2)

    for o, a in opts:
        if o == "-i":
            config.imgpath = os.path.abspath(a)
        elif o == "-l":
            try:
                config.limit = int(a)
            except ValueError:
                print("option -l requires integer")
                sys.exit(2)
        elif o == "-b":
            config.bmethod = True
        elif o == "-t":
            try:
                if (float(a) > 0 and float(a) <= 1):
                    config.threshold = float(a)
                else:
                    print("option -t requires number between 0 and 1")
                    sys.exit(2)
            except ValueError:
                print("option -t requires number between 0 and 1")
                sys.exit(2)
        else:
            assert False, "unhandled option"


def main():
    handle_args()
    config.filename = config.update_filename()
    config.img = get_image()
    config.res, config.width, config.height = set_res()

    if config.bmethod:
        htmlString, cssString = convert_bfs()
    else:
        cssString = convert_img()
        htmlString = write_html()

    write_to_css(cssString)
    write_to_HTML(htmlString)

    # open htmlfile when finished
    os.startfile(os.path.abspath(
        f"output/{'b' if config.bmethod else 'p'}/{config.filename}.html"), 'open')


if __name__ == '__main__':
    main()
