import serial
import cv2
import apriltag

#connect to controller board serial ports
devices = serial.Serial('[arduino port]', 9600)

while True:
    devData = devices.readline().decode().strip().split(',')
    #provides controller output as a list

#read camera data

devices.close()

