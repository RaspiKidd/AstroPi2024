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

image = [
    e,e,e,e,e,e,e,e,
    e,e,b,b,b,b,e,e,
    b,b,e,b,b,e,b,b,
    e,b,b,b,b,b,b,e,
    e,e,b,g,g,b,e,e,
    b,e,p,b,b,p,e,b,
    b,b,b,b,b,b,b,b,
    e,b,b,b,b,b,b,e]

# Display the image
sense.set_pixels(image)