from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(0)

sense.color.gain = 60
sense.color.integration_cycles = 64

g = (102, 255, 51)
o = (255, 102, 0)
f = (255, 133, 51)
b = (51, 153, 255)
y = (255, 235, 153)
bl = (0, 0, 0)

t = (51, 173, 255)
l = (255, 51, 133)
d = (128, 0, 51)
z = (255, 153, 194)


for i in range(28):
    rgb = sense.color
    c = (rgb.red, rgb.green, rgb.blue)


    image1 = [
    b,b,b,f,f,f,f,o,
    b,b,f,f,bl,f,f,b,
    b,b,b,b,y,f,f,o,
    b,b,b,y,y,y,f,b,
    b,b,b,y,y,y,f,b,
    b,g,b,b,y,f,f,g,
    b,g,o,b,b,f,o,g,
    g,g,g,o,o,o,g,g]
    

    image2 = [
    b,z,b,b,b,b,z,b,
    z,b,b,b,b,b,b,z,
    z,l,l,l,l,l,l,z,
    b,l,bl,l,l,bl,l,b,
    b,l,l,bl,bl,l,l,b,
    d,d,l,l,l,l,d,d,
    b,d,d,d,d,d,d,b,
    b,d,b,b,b,b,d,b]
    
    sense.set_pixels(image1)
    sleep (3)
    sense.set_pixels(image2)
    sleep (3)