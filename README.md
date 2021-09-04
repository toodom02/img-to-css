# IMG-TO-CSS

img-to-css converts an image into pure CSS, generating and displaying in an HTML file.

There are currently 2 different modes. The default draws CSS box-shadows pixel-by-pixel; This tends to be very performance heavy for the browser to display. The alternative `-b` uses BFS to find all areas of similar colour, and creates an solid colour HTML element with CSS clip-path to define the polygon. This is much slower to create, but tends to be faster for the browser to render.

## Setup

1. Install `Python 3.8` or greater
2. Run `pip install -r requirements.txt` to install all requirements
3. Run `python run.py`

## Usage and Options

`python run.py` will generate a random CSS file from the small selection of example images found in `/media`.

* `-i arg` will take a custom image file as input.

    e.g 
    
        python run.py -i path/to/img.jpg

* `-l arg` will set the maximum no. of pixels. `-l 0` to disable limit. Default value for pixel-by-pixel is `50000`.

    e.g.
        
        python run.py -l 75000

* `-b` will use a BFS approach, rather than pixel-by-pixel. Output files can be found in the `/output/b` directory if enabled, otherwise `/output/p`.

    e.g. 

        python run.py -b

* `-t arg` will set the threshold value for similar colours, used in the BFS approach on a scale `0 - 1` with `1` being the same colour. Default value is `0.95`.

    e.g.

        python run.py -b -t 0.85

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

- MIT license
- Copyright (c) 2021 Dominic Too