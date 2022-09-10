import board
import neopixel

from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.color import ORANGE

# Update to match the pin connected to your NeoPixels
pixel_pin = board.D18
# Update to match the number of NeoPixels you have connected
pixel_num = 24

pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.2, auto_write=False)
solid = Solid(pixels, color=ORANGE)
animations = AnimationSequence(solid, auto_clear=True)

while True:
    animations.animate()
