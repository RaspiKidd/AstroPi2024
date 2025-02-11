from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.set_rotation(270)
sense.colour.gain = 60
sense.colour.integration_cycles = 64

c = (25, 25, 112)
a = (255, 255, 255)
t = (255, 140, 0)
r = (0, 0, 0)

for i in range(28):
    rgb = sense.colour
    c = (rgb.red, rgb.green, rgb.blue)

    image = [
    t, a, t, c, c, t, a, t,
    t, a, t, c, c, t, a, t,
    t, t, t, t, t, t, t, t,
    t, a, r, t, t, r, a, t,
    t, t, t, t, t, t, t, t,
    a, a, a, r, r, a, a, a,
    c, a, a, a, a, a, a, c,
    c, c, a, a, a, a, c, c]

    sense.set_pixels(image)