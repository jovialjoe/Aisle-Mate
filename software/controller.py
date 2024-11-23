import pygame
import serial
import time
import tkinter as tk
from product_search_ui import aisle_robot_nav, bin_robot_nav, april_tag_id, ProductSearchApp

# Initialize serial communication with Arduino
arduino = serial.Serial('/dev/ttyUSB0', 9600)  # Adjust port as needed
time.sleep(2)  # Wait for Arduino to reset

# Initialize Pygame for Xbox controller input



def map_value(value, in_min, in_max, out_min, out_max):
    """Map a value from one range to another."""
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

try:
    root = tk.Tk()
    app = ProductSearchApp(root)
    root.mainloop()

    while True:

        while aisle_robot_nav:

            # Map joystick values to motor speed range (0 to 255)
            left_motor_speed = map_value(.7, -1, 1, 0, 255)
            right_motor_speed = map_value(.7, -1, 1, 0, 255)
            arduino.write(f"L{left_motor_speed}R{right_motor_speed}\n".encode())
            time.sleep(0.4)
            aisle_robot_nav -= 1
            
        break

        # Send motor speeds to Arduino
        

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting program.")

finally:
    arduino.close()
    pygame.quit()

