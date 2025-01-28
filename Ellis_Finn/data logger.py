from sense_hat import SenseHat
from datetime import datetime
2WRITE_FREQUENCY = 100
def file_setup(filename):
    header =["temp_h", "temp_p",humidity","pressure","pitch","roll","yaw","mag_x","mag_y","mag_2","accel_x'
    with open (filename,"w") as f:
        f.write(",".join(str(value) for value in header)+ "\n")
    log_data():
    output_string = ",".join(str(value) for value in sense_data)
    batch_data.append(output_string)
    get_sense_data():
    sense_data=[]
    
    sense_data.append(sense.get_temperature_from_humidity())
    sense_data.append(sense.get_temerature_from_pressure())
    sense_data.append(sense.get_humidity())
    sense_data.append(sense.get_pressure())
    yaw,pitch,roll = sense.get_orientation().values()
    sense_data.extend([pitch,roll,yaw])
    
    mag_x,mag_y,mag_z = sense.get_compass_raw().values()
    sense_data.extend([mag_x,mag_y,mag_z])
    
    x,y,z = sense.get_accelerometer_raw().values()
    sense_data.extend([x,y,z])
    
    gyro_x,gyro_y,gyro_z = sense.get_gyroscope_raw().values()
    sense_data.extend([gyro_x,gyro_y,gyro_z])
    