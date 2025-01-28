from sense_hat import SenseHat
from datetime import datetime
FILENAME = "
WITE_FREQUENCY  = 100
def file_setup(filename):
    header =["temp_h","temp_p", "humidity", "pressure", "pitch", "roll","yaw", "mag_x", "mag_y", "mag_z", "accel_x"
             
    with open (filename, "w") as f:
             f.write(",".join(str(value) for value in header) + "\n")
             
def log_data():
    output_string = ",".join(str(value) for value in sense_data)
    batch_data.append(output_string)
             
def get_sense_data():
    sense_data=[]
  
    sense_data.append(sense.get_temperaure_from_humidity())
    sense_date.append(sense.get_temperaure_from_pressure())
    sense_data.append(sense.get_humidity())
    sense_data.append(sense.get_pressure())
             
    yaw,pitch,roll = sense.get_orientation().valuses()