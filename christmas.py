import time

import board
import neopixel

try:
    import urandom as random
except ImportError:
    import random

bright_div = 20
numpix = 24  # Number of NeoPixels
pixpin = board.D18
# Pin where NeoPixels are connected
strip = neopixel.NeoPixel(pixpin, numpix, brightness=1, auto_write=False)
colors = [
    [232, 100, 255],  # Purple
    [200, 200, 20],  # Yellow
    [30, 200, 200],  # Blue
    [0, 255, 0], # Green
    [255, 0, 0], # Red
]

max_len=5
min_len = 2
#pixelnum, posn in flash, flash_len, direction
flashing = []

num_flashes = 5

for i in range(num_flashes):
    pix = random.randint(0, numpix - 1)
    col = random.randint(1, len(colors) - 1)
    flash_len = random.randint(min_len, max_len)
    flashing.append([pix, colors[col], flash_len, 0, 1])

strip.fill((0,0,0))

while True:
    strip.show()
    for i in range(num_flashes):
        #print(flashing[i])
        pix = flashing[i][0]
        brightness = (flashing[i][3]/flashing[i][2])
        colr = (int(flashing[i][1][0]*brightness),
                int(flashing[i][1][1]*brightness),
                int(flashing[i][1][2]*brightness))
        strip[pix] = colr
        if flashing[i][2] == flashing[i][3]:
            flashing[i][4] = -1
        if flashing[i][3] == 0 and flashing[i][4] == -1:
            pix = random.randint(0, numpix - 1)
            col = random.randint(0, len(colors) - 1)
            flash_len = random.randint(min_len, max_len)
            flashing[i] = [pix, colors[col], flash_len, 0, 1]
        flashing[i][3] = flashing[i][3] + flashing[i][4]
    time.sleep(0.1)


