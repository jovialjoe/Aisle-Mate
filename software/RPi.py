import serial
import time
import serial.tools.list_ports
#import cv2
#import numpy as np
#from apriltag import apriltag
from product_search_backend import find_aisle_bin
from product_search_ui import ProductSearchApp

def find_usb_serial_ports():
    #Finds and returns a list of USB serial ports on the Raspberry Pi

    ports = list(serial.tools.list_ports.comports())
    usb_ports = [port for port in ports if "USB" in port.description]
    return usb_ports

#connect to controller board serial ports
devices = serial.Serial(find_usb_serial_ports[0], 9600)

def aisleDrive(aisle):
    driveTime = aisle * 5 #constant: 5 seconds per aisle
    startTime = time.time()
    endTime = 0
    elapsedTime = 0
    while(elapsedTime < driveTime):
        devices.write(b'75,75')
        endTime = time.time()
        elapsedTime = startTime - endTime

def binDrive(bin):
    driveTime = bin * 1.5 #constant: 1.5 seconds per bin
    startTime = time.time()
    endTime = 0
    elapsedTime = 0
    while(elapsedTime < driveTime):
        devices.write(b'75,75')
        endTime = time.time()
        elapsedTime = startTime - endTime

def aisleTurn():
    startTime = time.time()
    endTime = 0
    elapsedTime = 0
    while(elapsedTime < 1.25):
        devices.write(b'0,75')
        endTime = time.time()
        elapsedTime = startTime - endTime

while True:
    devData = devices.readline().decode().strip().split(',')
    #provides controller output as a list
    obstruction = False
    sensorVals = devData[0:3]
    encoder1 = devData[4]
    encoder2 = devData[5]

    for value in sensorVals:
        if(True):
            if(value < 100):
                obstruction = True

    aisleDrive(find_aisle_bin[0])
    aisleTurn
    binDrive(find_aisle_bin[1])

    '''
    if(obstruction == True):
        #turn until obstruction is out of view
        devices.write(b'0,50')
    else:
        devices.write(b'50,50')
    '''

    devices.close()

    '''
    #Apriltag scanning:
    #detector = apriltag.Detector()

    #connect to camera:
    #cam = cv2.VideoCapture(0)
    #imagepath = 'test.jpg'
    #image = cv2.imread(imagepath, cv2.IMREAD_GRAYSCALE)
    #detector = apriltag("tagStandard41h12")

    #detections = detector.detect(image)
    '''