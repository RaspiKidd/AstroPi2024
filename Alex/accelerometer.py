from sense_hat import SenseHat
sense = SenseHat()
while True:
    pitch, roll, yaw = sense.get_orientation().values()
    print("pitch=%s, roll=%s, yaw=%s" % (pitch,yaw,roll))
    from sense_hat import SenseHat
    sense = SenseHat()
    while True:
        x, y, z = sense.get_accelerometer_raw().values()
        x=round(x, 0)
        y=round(y, 0)
        z=round(z, 0)
        print("x=%s, y=%s, z=%s" % (x, y, z)) 