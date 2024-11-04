import serial

#pull from controller board serial ports
devices = serial.Serial('', 9600)

#pull from rpi
#camera data

devData = devices.readline()