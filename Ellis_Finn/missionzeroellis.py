from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(270)

sense.color.gain = 60
sense.color.integration_cycles = 64

a = (225, 225, 225)
g = (0, 204,0)
d = (51, 204, 0)
r = (0, 153, 0)
b = (51, 204, 255)
l = (0, 0, 0)


for i in range(28):
    rgb = sense.color
    c = (rgb.red, rgb.green, rgb.blue)
    sleep(1)


image1 = [
    b, g, g, g, g, b, b, b,
    g, l, g, l, g, b, b, b,
    g, g, g, g, g, b, b, b,
    b, b, d, d, g, b, b, b,
    b, g, a, g, g, b, b, b,
    b, b, a, a, g, b, g, b,
    b, b, a, a, g, g, b, b,
    r, r, g, r, g, r, r, r]
    

image2 = [
    b, g, g, g, g, b, b, b,
    g, l, g, l, g, b, b, b,
    g, g, g, g, g, b, b, b,
    b, b, d, d, g, b, b, b,
    b, g, a, g, g, b, b, b,
    b, b, a, a, g, b, g, b,
    b, b, a, a, g, g, b, b,
    r, r, g, r, g, r, r, r]

sense.set_pixels(image1)

