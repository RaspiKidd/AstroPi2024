from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(270)

sense.color.gain = 60
sense.color.integration_cycles = 64

g = (102, 255, 51)
o = (255, 102, 0)
f = (255, 133, 51)
b = (51, 153, 255)
y = (255, 235, 153)
bl = (0, 0, 0)



for i in range(28):
    rgb = sense.color
    c = (rgb.red, rgb.green, rgb.blue)
    sleep(1)


image1 = [
    b,b,b,f,f,f,f,o,
    b,b,f,f,bl,f,f,b,
    b,b,b,b,y,f,f,o,
    b,b,b,y,y,y,f,b,
    b,b,b,y,y,y,f,b,
    b,g,b,b,y,f,f,g,
    b,g,o,b,b,f,o,g,
    g,g,g,o,o,o,g,g]
    
    
sense.set_pixels(image1)
   

