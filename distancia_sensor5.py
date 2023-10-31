from machine import Pin, PWM
import time
trig = Pin(17, Pin.OUT)
echo = Pin(16, Pin.IN, Pin.PULL_DOWN)
led = Pin('LED', Pin.OUT)
buzzer = PWM(Pin(15))
buzzer2 = PWM(Pin(1))

buzzer.freq(500)
buzzer2.freq(1000)



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
    if (distance < 30):
        led.value(1)
        buzzer.duty_u16(1000)
        time.sleep(0.2)
    elif (distance < 10):
        led.value(1)
        buzzer2.duty_u16(1000)
        time.sleep(0.2)
    else:
        led.value(0)
        buzzer.duty_u16(0)
        time.sleep(0.2)