import serial
import time
import serial.tools.list_ports
import tkinter as tk
import threading
import cv2
import numpy as np
from apriltag import Detector
from product_search_ui import aisle_robot_nav, bin_robot_nav, ProductSearchApp

def find_usb_serial_ports():
    # Finds and returns a list of USB serial ports on the Raspberry Pi
    ports = list(serial.tools.list_ports.comports())
    usb_ports = [port for port in ports if "USB" in port.description]
    return usb_ports

def run_robot_control(devices):
    while True:
        devData = devices.readline().decode().strip().split(',')
        obstruction = False
        sensorVals = devData[0:3]
        encoder1 = devData[4]
        encoder2 = devData[5]

        for value in sensorVals:
            if int(value) < 100:
                obstruction = True

        aisleDrive(int(aisle_robot_nav))
        aisleTurn()
        binDrive(int(bin_robot_nav))

        # Add more logic here for robot control...

def aisleDrive(aisle):
    driveTime = aisle * 5  # constant: 5 seconds per aisle
    startTime = time.time()
    while time.time() - startTime < driveTime:
        devices.write(b'75,75')

def binDrive(bin):
    driveTime = bin * 1.5  # constant: 1.5 seconds per bin
    startTime = time.time()
    while time.time() - startTime < driveTime:
        devices.write(b'75,75')

def aisleTurn():
    startTime = time.time()
    while time.time() - startTime < 1.25:
        devices.write(b'0,75')

if __name__ == "__main__":
    # Tkinter GUI
    root = tk.Tk()
    app = ProductSearchApp(root)
    root.mainloop()
    '''
    # Connect to the serial port
    devices = serial.Serial(find_usb_serial_ports()[0].device, 9600)

    # Start the robot control in a separate thread
    robot_thread = threading.Thread(target=run_robot_control, args=(devices,))
    robot_thread.daemon = True  # Ensures the thread exits when the main program exits
    robot_thread.start()

    # Apriltag scanning
    detector = apriltag.Detector()

    # Open the camera
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Error: Could not open camera.")
        exit()

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detections = detector.detect(gray)

        # Handle detections
        for detection in detections:
            print("Detected tag: ", detection.tag_id)

        # Optional: Display the video feed with detections (if needed)
        cv2.imshow("Camera", frame)

        # Exit condition to stop the video feed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
    devices.close()
    '''
