import board
import neopixel
import RPi.GPIO as GPIO
import time

# How many pixels are in the WS2812b strip?
MAX_PIXELS = 16

# How long should we shine the pixels (in seconds)?
SHINE_TIMER = 12

# How bright should the LEDs be?
BRIGHTNESS = 1.0

# What GPIO pin is associated with a condition?
MOTION_DETECT_INPUT_PIN = 20 # Physical pin 38
DARK_INDICATOR_PIN = 21 # Physical pin 40

# Use the board internal definition for this
LED_STRIP_OUTPUT_PIN = board.D18

# Colors
WHITE = (255, 255, 255)
OFF = (0, 0, 0)


pixels = neopixel.NeoPixel(LED_STRIP_OUTPUT_PIN, MAX_PIXELS,
                          brightness=BRIGHTNESS)

GPIO.setwarnings(False)

# Refer pins by their sequence number on the board
GPIO.setmode(GPIO.BCM)

# Read output from PIR motion sensor
GPIO.setup(MOTION_DETECT_INPUT_PIN, GPIO.IN)

# Configure the light sensor
GPIO.setup(DARK_INDICATOR_PIN, GPIO.IN)

while True:
    try:
        # IF it is nighttime, switch on the DARK indicator
        if GPIO.input(DARK_INDICATOR_PIN):
            # print("Room DARK")
            if GPIO.input(MOTION_DETECT_INPUT_PIN):
                # print("Motion detected!!")
                pixels.fill(WHITE)
                time.sleep(SHINE_TIMER)
                pixels.fill(OFF)
            else:
                # print("DARK but no motion.")
                pass
        else:
            # print("room NOT dark")
            pass
    except KeyboardInterrupt:
        pixels.fill(OFF)
        exit()
