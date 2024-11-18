import serial
import serial.tools.list_ports

def detect_serial_port():
    """
    Detects available serial ports and returns the first one.
    """
    ports = serial.tools.list_ports.comports()
    if not ports:
        print("No serial ports detected.")
        return None

    for port in ports:
        print(f"Found serial port: {port.device}")
    return ports[0].device

def read_serial_data(port, baudrate=9600, timeout=1):
    """
    Reads data from a serial port and prints it to the console.

    Parameters:
    - port (str): The serial port to connect to (e.g., "COM3" or "/dev/ttyUSB0").
    - baudrate (int): The baud rate for the serial communication. Default is 9600.
    - timeout (int): The read timeout in seconds. Default is 1 second.
    """
    try:
        # Open the serial connection
        with serial.Serial(port, baudrate, timeout=timeout) as ser:
            print(f"Connected to {port} at {baudrate} baud.")
            
            while True:
                # Read a line of data from the serial port
                data = ser.readline().decode('utf-8').strip()
                
                if data:  # Print non-empty data
                    print(f"Received: {data}")
                    
    except serial.SerialException as e:
        print(f"Error: Could not open serial port {port}. {e}")
    except KeyboardInterrupt:
        print("\nExiting program.")

if __name__ == "__main__":
    port = detect_serial_port()
    if port:
        read_serial_data(port=port, baudrate=9600)
    else:
        print("No serial port available. Exiting.")
