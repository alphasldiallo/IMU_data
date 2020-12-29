from board import SDA, SCL
from imu_mpu6050 import MPU6050
import busio
import time
import csv
import json
from socket_client import MySocket



i2c = busio.I2C(SCL, SDA)
IMU=MPU6050(i2c)
print(IMU.whoami)

while True:
    s = MySocket()
    s.connect(host="192.168.192.31", port=1223)
    acc =IMU.get_accel_data(g=True)
    gyro = IMU.get_gyro_data()
    tmp_dict = {"acc_x":acc["x"], "acc_y":acc["y"], "acc_z":acc["z"], "gyro_x":gyro["x"], "gyro_y":gyro["y"], "gyro_z":gyro["z"] }
#       print(str(len(data)/1000*100)+"%")
    time.sleep(0.1)
    tmp_json = json.dumps(tmp_dict)
    s.send(tmp_json)
    s.close()
    print("Sent!")
