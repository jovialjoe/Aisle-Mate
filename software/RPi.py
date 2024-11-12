import serial
import time
#import cv2
#import numpy as np
#from apriltag import apriltag
from product_search_backend import find_aisle_bin
from product_search_ui import ProductSearchApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = ProductSearchApp(root)
    target = find_aisle_bin(app.get_entry())
    root.mainloop()

#connect to controller board serial ports
devices = serial.Serial('[arduino port]', 9600)

def calculateDist(sensorVal):
    return ((float)(sensorVal) * 0.0343) / 2
    # distance = sensor output * speed of sound / 2
    # speed of sound in centimeter per microsecond

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

    for values in sensorVals:
        if(True):
            if(calculateDist(devData[values]) < 100):
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