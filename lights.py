"""
This controls a long (8.4 meter) ws2812b strip using a Raspberry Pi. There are a total of 506 pixels in the strip.
In addition to the power supplied by the RPi, there is an external power supply. The external power supply is
connected at both ends of the strip. It supplies 5 Volts at a maximum of 40 amps. Each connection to the strip
has about 3 meters of wire to connect to the power supply.
"""
import board
import neopixel
import RPi.GPIO as GPIO
import time

# How many pixels are in the WS2812b strip?
MAX_PIXELS = 506

# How bright should the LEDs be?
BRIGHTNESS = 0.4

# How long should we shine the LEDs?
SHINE_TIMER = 3600

# What GPIO pin is associated with a condition?
DARK_INDICATOR_PIN = 21  # Physical pin 40

# Use the board internal definition for this
LED_STRIP_OUTPUT_PIN = board.D18

# Colors
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

pixels = neopixel.NeoPixel(LED_STRIP_OUTPUT_PIN, MAX_PIXELS, brightness=BRIGHTNESS)

GPIO.setwarnings(False)

# Refer pins by their sequence number on the board
GPIO.setmode(GPIO.BCM)

# Configure the light sensor
GPIO.setup(DARK_INDICATOR_PIN, GPIO.IN)

while True:
    try:
        if GPIO.input(DARK_INDICATOR_PIN):
            pixels.fill(WHITE)
            # Put this here because there tends to be a flickering effect at twilight and sunrise.
            # So, make the strip stay on continuously for a time while the light growing or receding
            time.sleep(SHINE_TIMER)
        else:
            pixels.fill(OFF)
    except KeyboardInterrupt:
        pixels.fill(OFF)
        exit()
