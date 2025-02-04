from sense_hat import SenseHat
from datetime import datetime
#sense = SenseHat()
FILENAME = ""
WRITE_FREQUENCY = 100
def file_setup(filename):
    header =["temp_h", "temp_p","humidity","pressure","pitch","roll","yaw","mag_x","mag_y","mag_z","accel_x"]
    with open (filename,"w") as f:
        f.write(",".join(str(value) for value in header)+ "\n")
def log_data():
    output_string = ",".join(str(value) for value in sense_data)
    batch_data.append(output_string)
def get_sense_data():
    sense_data=[]
    
    sense_data.append(sense.get_temperature_from_humidity())
    sense_data.append(sense.get_temperature_from_pressure())
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
    
    sense_data.append(datetime.now())
    return sense = SenseHat()
batch_data= []

if FILENAME == "":
    filename = "SenseLog-"+str(datetime.now())+".csv"
else:
    filename = FILENAME+"-"+str(datetime.now())+".csv"
    
file_setup(filename)

while True:
    sense_data = get_sense_data()
    log_data()
    
    if len(batch_data) >= WRITE_FREQUENCY:
        print ("Writing to file..")
        with open(filename,"a") as f:
            for line in batch_data:
                f.write(line + "\n")
            batch_data = []



    