from hcsr04 import HCSR04
from SSD1306 import SSD1306_I2C
from machine import Pin, I2C

LED25 = Pin(25, Pin.OUT)
LED25.value(1)

sensor = HCSR04(trigger_pin = 4, echo_pin = 5)
i2c_2 = I2C(0,scl=Pin(17), sda=Pin(16), freq=400000) 

d = SSD1306_I2C(128,64,i2c_2)

while 1:
    distance = sensor.distance_cm()
    d.text(str(distance),10,30)
    d.show()
    d.fill(0)
    print(distance)
