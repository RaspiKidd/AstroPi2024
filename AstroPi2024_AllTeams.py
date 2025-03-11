from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.set_rotation(0)
sense.colour.gain = 60
sense.colour.integration_cycles = 64

# Alex's Colours
o = (252, 127, 3)
b = (31, 11, 1)
g = (16, 156, 6)
w = (235, 255, 183)
y = (115, 103, 16)
f1 = (174, 127, 3)
f2 = (205, 46, 3)

# Gordon's Colours
bg = (0, 163, 204) 
p = (255, 77, 136) 
e = (255, 255, 255)
gr = (34, 139, 34)
og = (178, 34, 34)

# Finn's Colours
gf = (102, 255, 51)
of = (255, 102, 0)
f = (255, 133, 51)
bf = (51, 153, 255)
yf = (255, 235, 153)
t = (51, 173, 255)
l = (255, 51, 133)
d = (128, 0, 51)
z = (255, 153, 194)

# Ellis's Colours
ge = (0, 204,0)
de = (51, 204, 0)
r = (0, 153, 0)
be = (51, 204, 255)
ee = (255, 0, 0)

#Clear screen
x = (0, 0, 0)

# Alex's Images
alexImg1= [
    w, w, w, w, g, w, w, w,
    w, w, w, g, g, w, w, w,
    w, w, g, g, o, g, w, w,
    w, o, o, o, o, o, o, w,
    o, o, b, o, o, b, o, o,
    o, o, o, o, o, o, o, o,
    o, o, b, b, b, b, o, o,
    w, o, o, o, o, o, o, w]
    
alexImg2= [
    w, w, w, w, g, w, w, w,
    w, w, w, g, g, w, w, w,
    w, w, g, g, o, g, w, w,
    w, o, o, o, o, o, o, w,
    o, o, y, o, o, y, o, o,
    o, o, o, o, o, o, o, o,
    o, o, y, y, y, y, o, o,
    w, o, o, o, o, o, o, w]

alexImg3= [
    w, w, w, w, g, w, w, w,
    w, w, w, g, g, w, w, w,
    w, w, g, g, o, g, w, w,
    w, o, o, o, o, o, o, w,
    o, o, f1, o, o, f1, o, o,
    o, o, o, o, o, o, o, o,
    o, o, f1, f1, f1, f1, o, o,
    w, o, o, o, o, o, o, w]

alexImg4= [
    w, w, w, w, g, w, w, w,
    w, w, w, g, g, w, w, w,
    w, w, g, g, o, g, w, w,
    w, o, o, o, o, o, o, w,
    o, o, f2, o, o, f2, o, o,
    o, o, o, o, o, o, o, o,
    o, o, f2, f2, f2, f2, o, o,
    w, o, o, o, o, o, o, w]

# Gordon's Images
gordonImg1 = [
    e,e,e,e,e,e,e,e,
    e,e,bg,bg,bg,bg,e,e,
    bg,bg,e,bg,bg,e,bg,bg,
    e,bg,bg,bg,bg,bg,bg,e,
    e,e,bg,x,x,bg,e,e,
    bg,e,p,bg,bg,p,e,bg,
    bg,bg,bg,bg,bg,bg,bg,bg,
    e,bg,bg,bg,bg,bg,bg,e]

gordonImg2 = [
    bg,bg,bg,bg,bg,bg,bg,bg,
    bg,bg,og,bg,bg,bg,bg,bg,
    bg,bg,og,og,og,og,og,bg,
    bg,gr,og,og,og,og,og,og,
    bg,gr,og,og,og,og,og,og,
    bg,bg,og,og,og,og,og,bg,
    bg,bg,og,bg,bg,bg,bg,bg,
    bg,bg,bg,bg,bg,bg,bg,bg]

# Finn's Images
finnImg1 = [
    bf,bf,bf,f,f,f,f,of,
    bf,bf,f,f,x,f,f,bf,
    bf,bf,bf,bf,yf,f,f,of,
    bf,bf,bf,yf,yf,yf,f,bf,
    bf,bf,bf,yf,yf,yf,f,bf,
    bf,gf,bf,bf,y,f,f,gf,
    bf,gf,of,bf,bf,f,of,gf,
    gf,gf,gf,of,of,of,gf,gf]
    

finnImg2 = [
    bf,z,bf,bf,bf,bf,z,bf,
    z,bf,bf,bf,bf,bf,bf,z,
    z,l,l,l,l,l,l,z,
    bf,l,x,l,l,x,l,bf,
    bf,l,l,x,x,l,l,bf,
    d,d,l,l,l,l,d,d,
    bf,d,d,d,d,d,d,bf,
    bf,d,bf,bf,bf,bf,d,bf]

# Ellis's Images
ellisImg1 = [
    be, ge, ge, ge, ge, be, be, be,
    ge, x, ge, x, ge, be, be, be,
    ge, ge, ge, ge, ge, be, be, be,
    be, be, de, de, ge, be, be, be,
    be, ge, e, ge, ge, be, ge, be,
    be, be, e, e, ge, be, ge, be,
    be, be, e , e, ge, ge, be, be,
    r, r, ge, r, ge, r, r, r]
    
ellisImg2 = [
    be, ge, ge, ge, ge, be, be, be,
    ge, ee, ge, ee, ge, be, be, be,
    ge, ge, ge, ge, ge, be, be, be,
    be, be, de, de, ge, be, be, be,
    be, ge, e, ge, ge, be, be, ge,
    be, be, e, e, ge, be, ge, be,
    be, be, e, e, ge, ge, be, be,
    r, r, ge, r, ge, r, r, r]

for i in range (1):
    # Alex's Animation
    print("starting")
    sleep(0.2)
    sense.show_message("A", text_colour=[255,255,255], back_colour=[0,0,0])
    sense.set_pixels(alexImg1)
    sleep(1)
    sense.set_pixels(alexImg2)
    sleep(1)
    sense.set_pixels(alexImg3)
    sleep(1)
    sense.set_pixels(alexImg4)
    sleep(1)
    sense.set_pixels(alexImg3)
    sleep(1)
    sense.set_pixels(alexImg2)
    sleep(1)
    sense.set_pixels(alexImg1)
    sleep(1)
    sense.clear(x)
    sleep(1)
    # Gordon's Animation
    sense.show_message("G", text_colour=[255,255,255], back_colour=[0,0,0])
    for i in range (2):
        sense.set_pixels(gordonImg1)
        sleep(1)
        sense.set_pixels(gordonImg2)
        sleep(1)
    
    sense.clear(x)
    sleep(1)
    
    #Finn's Animation
    sense.show_message("F", text_colour=[255,255,255], back_colour=[0,0,0])
    for i in range (2):
        sense.set_pixels(finnImg1)
        sleep(1)
        sense.set_pixels(finnImg2)
        sleep(1)
        
    sense.clear(x)
    sleep(1)
    
    # Ellis's Animation
    sense.show_message("E", text_colour=[255,255,255], back_colour=[0,0,0])
    for i in range (2):
        sense.set_pixels(ellisImg1)
        sleep(1)
        sense.set_pixels(ellisImg2)
        sleep(1)
    
    sense.clear(x)
    sleep(1)
    print("finished")

