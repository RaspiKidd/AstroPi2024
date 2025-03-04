# Import the libraries
from sense_hat import SenseHat
from time import sleep

# set up the Sense HAT
sense = SenseHat()
sense.set_rotation(0)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.intergration_cycles = 64 # The interval at which the reading will be taken

# Add colour variables and image

b = (0, 163, 204) # Diagram
g = (0, 0, 0) # Black
p = (255, 77, 136) # CornflowerBlue
e = (255, 255, 255)
gr = (34, 139, 34)
o = (178, 34, 34)

image1 = [
    e,e,e,e,e,e,e,e,
    e,e,b,b,b,b,e,e,
    b,b,e,b,b,e,b,b,
    e,b,b,b,b,b,b,e,
    e,e,b,g,g,b,e,e,
    b,e,p,b,b,p,e,b,
    b,b,b,b,b,b,b,b,
    e,b,b,b,b,b,b,e]

image2 = [
    b,b,b,b,b,b,b,b,
    b,b,o,b,b,b,b,b,
    b,b,o,o,o,o,o,b,
    b,gr,o,o,o,o,o,o,
    b,gr,o,o,o,o,o,o,
    b,b,o,o,o,o,o,b,
    b,b,o,b,b,b,b,b,
    b,b,b,b,b,b,b,b]

while True:
    # Display the image
    sense.set_pixels(image1)
    sleep(1)
    sense.set_pixels(image2)
    sleep(1)