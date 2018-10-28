import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)

PIN_LIVING = 4
GPIO.setup(PIN_LIVING, GPIO.OUT)
living = GPIO.PWM(PIN_LIVING, 100)
living.start(0)
dc = 50
living.ChangeDutyCycle(dc)
PIN_FIREPLACE = 27
GPIO.setup(PIN_FIREPLACE, GPIO.OUT)
fire = GPIO.PWM(PIN_FIREPLACE, 30)
fire.start(0)
try:
    while 1:
        pass
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit(1)
