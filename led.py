from machine import Pin
import time

led = Pin('LED', Pin.OUT)

while True:
    led.value(1)
    time.sleep(0.2)
    led.value(0)
    time.sleep(0.5)