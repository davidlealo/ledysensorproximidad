from machine import Pin
import time
import gpiozero as gp

servo = gp.Servo(1)

trig = Pin(17, Pin.OUT)
echo = Pin(16, Pin.IN, Pin.PULL_DOWN)
led = Pin('LED', Pin.OUT)

while True:
    trig.value(0)
    time.sleep(0.1)
    trig.value(1)
    time.sleep_us(2)
    trig.value(0)
    while echo.value() ==0:
        pulse_start = time.ticks_us()
    while echo.value() == 1:
        pulse_end = time.ticks_us()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17165/1000000
    distance = round(distance,0)
    print('distance',"{:.0f}".format(distance),'cm')
    time.sleep(1)
    if (distance < 10):
        led.value(1)
        time.sleep(0.2)
    else:
        led.value(0)
        time.sleep(0.2)
    