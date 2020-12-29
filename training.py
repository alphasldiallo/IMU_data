from board import SDA, SCL
from imu_mpu6050 import MPU6050
import busio
import time
import csv

i2c = busio.I2C(SCL, SDA)
IMU=MPU6050(i2c)
print(IMU.whoami)

data = []
SAMPLES = 500
  
while(len(data)<SAMPLES):
    #print("Temperature is "+str(IMU.get_temp))
    #print(str(IMU.get_accel_data(g=True)["x"]))
    acc =IMU.get_accel_data(g=True)
    gyro = IMU.get_gyro_data()
    tmp_dict = {"acc_x":acc["x"], "acc_y":acc["y"], "acc_z":acc["z"], "gyro_x":gyro["x"], "gyro_y":gyro["y"], "gyro_z":gyro["z"] }
    data.append(tmp_dict)
    print(str(len(data)/SAMPLES*100)+"%")
    time.sleep(0.1)
    
    
with open("hadoken.csv", mode="w") as f:
    w = csv.DictWriter(f, data[0].keys())
    w.writeheader()
    for i in data:
        w.writerow(i)