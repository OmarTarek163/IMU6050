from mpu6050 import mpu6050
from time import sleep
import numpy as np

#intiallizations
imu = mpu6050(0x68)
cal_steps=10000
linear_x=[]
linear_y=[]
linear_z=[]
rot_x=[]
rot_y=[]
rot_z=[]
linear_x_mean=0
linear_y_mean=0
linear_z_mean=0
rot_x_mean=0
rot_y_mean=0
rot_z_mean=0

#calibration 
for i in range (cal_steps):
    accel_data = imu.get_accel_data()
    gyro_data = imu.get_gyro_data()
    
    linear_x.append = accel_data['x']
    linear_y.append = accel_data['y']
    linear_z.append = accel_data['z']
    rot_x.append = gyro_data['x']
    rot_y.append = gyro_data['y']
    rot_z.append = gyro_data['z']

for j in range (cal_steps):
    if j>100 :
        linear_x_mean = linear_x_mean+linear_x(j) 
        linear_y_mean = linear_y_mean+linear_y(j) 
        linear_z_mean = linear_z_mean+linear_z(j) 
        rot_x_mean = rot_x_mean+rot_x(j)
        rot_y_mean = rot_y_mean+rot_y(j)
        rot_z_mean = rot_z_mean+rot_z(j)
    

linear_x_mean=linear_x_mean/cal_steps
linear_y_mean=linear_y_mean/cal_steps
linear_z_mean=linear_z_mean/cal_steps
rot_x_mean=rot_x_mean/cal_steps
rot_y_mean=rot_y_mean/cal_steps
rot_z_mean=rot_y_mean/cal_steps

linear_x_offset = -linear_x_mean/8
linear_y_offset = -linear_y_mean/8
linear_z_offset = (16384-linear_z_mean)/8

print("linear acceleration in x direction mean value equals " + str(linear_x_mean))
print("linear acceleration in y direction mean value equals " + str(linear_y_mean))
print("linear acceleration in z direction mean value equals " + str(linear_z_mean))
print("rot acceleration around x direction mean value equals " + str(rot_x_mean))
print("rot acceleration around y direction mean value equals " + str(rot_y_mean))
print("rot acceleration around z direction mean value equals " + str(rot_z_mean))

