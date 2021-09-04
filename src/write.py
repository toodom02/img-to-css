from . import config


def write_to_css(css):
    f = open(
        f"output/{'b' if config.bmethod else 'p'}/{config.filename}.css", "w")
    f.write(css)
    f.close()


def write_to_HTML(html):
    f = open(
        f"output/{'b' if config.bmethod else 'p'}/{config.filename}.html", "w")
    f.write(html)
    f.close()
