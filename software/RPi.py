import serial
#import cv2
#import numpy as np
#from apriltag import apriltag

import product_search_ui 
import product_search_backend


if __name__ == "__main__":
    root = product_search_ui.tk.Tk()
    app = product_search_ui.ProductSearchApp(root)
    target = product_search_backend.find_aisle_bin(app.get_entry())
    root.mainloop()

#connect to controller board serial ports
devices = serial.Serial('[arduino port]', 9600)

def calculateDist(sensorVal):
    return ((float)(sensorVal) * 0.0343) / 2
    # distance = sensor output * speed of sound / 2
    # speed of sound in centimeter per microsecond

def aisleDrive(aisle):
    
    devices.write(b'0,75')

def binDrive(bin):
    return

while True:
    devData = devices.readline().decode().strip().split(',')
    #provides controller output as a list
    obstruction = False
    sensorVals = devData[0:3]
    encoder1 = devData[4]
    encoder2 = devData[5]

    for values in sensorVals:
        if(True):
            if(calculateDist(devData[values]) < 30):
                obstruction = True

    if(obstruction == True):
        #send back data to control - value from 0-100
        devices.write(b'0,50')
    else:
        devices.write(b'50,50')

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