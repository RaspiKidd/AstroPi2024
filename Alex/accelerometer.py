from sense_hat import SenseHat
sense = SenseHat()
while True:
    pitch, roll, yaw = sense.get_orientstion().values()
    print("pitch=%s, roll=%s, yaw=%s" % (pitch,yaw,roll))
    from sense_hat import SenseHat
    sense = SenseHat()
    while True:
        x, y, z = sense.get_accelerometer_raw().values()