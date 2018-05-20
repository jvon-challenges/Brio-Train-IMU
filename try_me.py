#!/usr/bin/env python3
# import python libraries
import time

# import rcpy library
# This automatically initizalizes the robotics cape
import rcpy 
import rcpy.mpu9250 as mpu9250    # we are using the motion sensor (mpu9250)

def train():

    rcpy.set_state(rcpy.RUNNING)
    mpu9250.initialize(enable_magnetometer = False)

    while True:
        data = mpu9250.read()
        print(data['gyro'][0],data['gyro'][1],data['gyro'][2])
        time.sleep(0.1)


if __name__ == "__main__":
    train()
