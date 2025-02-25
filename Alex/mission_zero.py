from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.set_rotation(0)
sense.colour.gain = 60
sense.colour.integration_cycles = 64

p = (212, 158, 125)
t = (255, 140, 0)
a = (255, 255, 255)
c = (0, 0, 0)
q = (255, 255, 0)
d = (100, 149, 237)

for i in range(28):
    rgb = sense.colour
    c = (rgb.red, rgb.green, rgb.blue)

    image = [
    a, a, q, q, q, q, a, a,
    a, q, q, q, q, q, q, a,
    q, q, q, p, q, q, q, a,
    q, q, d, p, p, d, p, a,
    a, q, p, p, p, p, q, a,
    a, a, d, d, d, d, a, a,
    a, p, c, c, c, c, p, a,
    a, a, t, a, a, t, a, a]

    sense.set_pixels(image)