
from SSD1306 import SSD1306_I2C
from machine import *
led = Pin(26, Pin.OUT)
led.on()
m = 'led'
i2c_2 = I2C(0,scl=Pin(17), sda=Pin(16), freq=400000) 
d = SSD1306_I2C(128,64,i2c_2)
d.fill(0)

d.text("Hello Pi Pico",12,30)
d.show()
