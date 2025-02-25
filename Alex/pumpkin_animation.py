from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.set_rotation(0)
sense.colour.gain = 60
sense.colour.integration_cycles = 64

o = (252, 127, 3)
b = (31, 11, 1)
g = (16, 156, 6)
w = (235, 255, 183)
f1 = (255, 59, 5)
f2 = (255, 46, 3)

for i in range(28):
    rgb = sense.colour
    c = (rgb.red, rgb.green, rgb.blue)

    image1= [
    w, w, w, w, g, w, w, w,
    w, w, w, g, g, w, w, w,
    w, w, g, g, o, g, w, w,
    w, o, o, o, o, o, o, w,
    o, o, b, o, o, b, o, o,
    o, o, o, o, o, o, o, o,
    o, o, b, b, b, b, o, o,
    w, o, o, o, o, o, o, w]
    
image2= [
    w, w, w, w, g, w, w, w,
    w, w, w, g, g, w, w, w,
    w, w, g, g, o, g, w, w,
    w, o, o, o, o, o, o, w,
    o, o, f1, o, o, f1, o, o,
    o, o, o, o, o, o, o, o,
    o, o, f1, f1, f1, f1, o, o,
    w, o, o, o, o, o, o, w]

image3= [
    w, w, w, w, g, w, w, w,
    w, w, w, g, g, w, w, w,
    w, w, g, g, o, g, w, w,
    w, o, o, o, o, o, o, w,
    o, o, f2, o, o, f2, o, o,
    o, o, o, o, o, o, o, o,
    o, o, f2, f2, f2, f2, o, o,
    w, o, o, o, o, o, o, w]
    

sense.set_pixels(image1)
sleep(1)
sense.set_pixels(image2)
sleep(1)
sense.set_pixels(image3)
sleep(1)
sense.set_pixels(image2)
sleep(1)
sense.set_pixels(image1)