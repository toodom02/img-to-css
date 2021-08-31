
def write_to_css(filename, css):
    f = open(f"output/{filename}.css", "w")
    f.write(css)
    f.close()


def write_to_HTML(filename, html):
    f = open(f"output/{filename}.html", "w")
    f.write(html)
    f.close()
