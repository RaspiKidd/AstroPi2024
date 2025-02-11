from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(270)

sense.color.gain = 60
sense.color.integration_cycles = 64

g = (0, 191, 255) #deepskyblue

c = (0, 0, 0) # Black
a = (255, 255, 255) # White
t = (255, 140, 0) # Dark Orange

for i in range(28):
    rgb = sense.color
    c = (rgb.red, rgb.green, rgb.blue)
    sleep(1)


image1 = [
    t, a, t, c, c, t, a, t,
    t, a, t, c, c, t, a, t,
    t, t, t, t, t, t, t, t,
    t, a, c, t, t, c, a, t,
    t, t, t, t, t, t, t, t,
    a, a, a, c, c, a, a, a,
    c, a, a, a, a, a, a, c,
    c, c, a, a, a, a, c, c]

c = (100, 149, 237)
a = (255, 255, 255)
v = (255, 0, 0)
t = (255, 140, 0)
q = (255, 255, 0)
l = (0, 255, 127)
e = (0, 0, 205)

image2 = [
    
sense.set_pixels(image)
   
