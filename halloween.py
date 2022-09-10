import board
import neopixel

from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.color import (
    PURPLE,
    WHITE,
    AMBER,
    JADE,
    TEAL,
    PINK,
    MAGENTA,
    ORANGE,
)

# Update to match the pin connected to your NeoPixels
pixel_pin = board.D18
# Update to match the number of NeoPixels you have connected
pixel_num = 506

pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.2, auto_write=False)

solid = Solid(pixels, color=ORANGE)
blink = Blink(pixels, speed=0.5, color=JADE)
colorcycle = ColorCycle(pixels, speed=0.4, colors=[MAGENTA, ORANGE, TEAL])
chase = Chase(pixels, speed=0.1, color=WHITE, size=3, spacing=6)
comet = Comet(pixels, speed=0.01, color=PURPLE, tail_length=10, bounce=True)
pulse = Pulse(pixels, speed=0.1, color=AMBER, period=3)


animations = AnimationSequence(solid,auto_clear=True)

while True:
    animations.animate()

