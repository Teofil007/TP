from machine import *
from utime import *
from SSD1306 import SSD1306_I2C
LED = Pin(25, Pin.OUT)
LED.value(1)
ENA = Pin(2, Pin.OUT)

IN1 = PWM(Pin(3, mode=Pin.OUT))
IN2 = PWM(Pin(4, mode=Pin.OUT))
IN1.freq(5000)
IN2.freq(5000)

x = ADC(Pin(27))
y = ADC(Pin(26))
i2c_2 = I2C(0,scl=Pin(17), sda=Pin(16), freq=400000)



d = SSD1306_I2C(128,64,i2c_2)
d.fill(0)


def moteur_gauche():
    
    ENA.value(1)
    IN1.duty_u16(x_val)
    IN2.duty_u16(0)
    d.fill(0)
    d.text('LEFT',10,30)
    d.show()

def moteur_droit():
    ENA.value(1)
    IN1.duty_u16(0)
    IN2.duty_u16(-(x_val*2)+ 600000)
    d.fill(0)
    d.text('Right',10,30)
    d.show()
   
def stop():

    IN1.duty_u16(0)
    IN2.duty_u16(0)
    d.fill(0)
    d.text('Stop',10,50)

    d.show()
    
while True:

    x_val = x.read_u16()
   
    if (x_val > 33000) :
        moteur_gauche()
    elif x_val < 31000:
        moteur_droit()

    else:
        stop()
    sleep(0.02)       
    print(x_val,",",y_val)
    










 
