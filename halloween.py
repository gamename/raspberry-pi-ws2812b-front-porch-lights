import board
import neopixel

# Update to match the pin connected to your NeoPixels
pixel_pin = board.D18
# Update to match the number of NeoPixels you have connected
pixel_num = 24

ORANGE =(253, 166, 0)
OFF = (0, 0, 0)

pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.2, auto_write=False)

pixels.fill(OFF)
try:
    while True:
        pixels.fill(ORANGE)
except KeyboardInterrupt:
        pixels.fill(OFF)
        exit()
