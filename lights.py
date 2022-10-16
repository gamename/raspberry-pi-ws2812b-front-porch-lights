"""
This controls a long (8.4 meter) ws2812b strip using a Raspberry Pi. There are a total of 506 pixels
 in the strip. In addition to the power supplied by the RPi, there is an external power supply. The
 external power supply is connected at both ends of the strip. It supplies 5 Volts at a maximum of
 40 amps. Each connection to the strip has about 3 meters of wire to connect to the power supply.
"""
import board
import neopixel
import RPi.GPIO as GPIO
import time

# How many pixels are in the WS2812b strip?
MAX_PIXELS = 506

# How bright should the LEDs be?
BRIGHTNESS = 0.10  # 10%

# How long (in seconds) should we shine the LEDs?
SHINE_TIMER = 300  # 5 minutes

# What GPIO pin is associated with a condition?
DARK_INDICATOR_PIN = 21  # Physical pin 40

# Use the board internal definition for this
LED_STRIP_OUTPUT_PIN = board.D18  # Physical pin 12

# Colors
ORANGE =(253, 166, 0)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

pixels = neopixel.NeoPixel(LED_STRIP_OUTPUT_PIN, MAX_PIXELS, brightness=BRIGHTNESS)

GPIO.setwarnings(False)

# Refer to pins by their Broadcom numbers
GPIO.setmode(GPIO.BCM)

# Configure the light sensor
GPIO.setup(DARK_INDICATOR_PIN, GPIO.IN)

while True:
    try:
        if GPIO.input(DARK_INDICATOR_PIN):
            pixels.fill(ORANGE)
        else:
            pixels.fill(OFF)

        # At twilight and sunrise, there is a very short (1 or 2 minute) period when the light
        # sensor cannot decide if it is light or dark.  This tends to cause the strip to flicker.
        # To avoid this, set a short timer to make the strip stay on (or off) for a period long
        # enough to avoid confusing the light sensor when the sun rises or sets.
        time.sleep(SHINE_TIMER)
    except KeyboardInterrupt:
        pixels.fill(OFF)
        exit()
