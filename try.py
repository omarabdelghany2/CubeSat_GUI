import serial

def receive_serial_data(port, baudrate=9600):
    try:
        ser = serial.Serial(port, baudrate)
        print(f"Listening on {port} at {baudrate} baudrate...")

        while True:
            # Read a line from the serial port
            data = ser.readline().decode('utf-8').strip()
            
            # Process the received data
            print(f"Received: {data}")

    except serial.SerialException as e:
        print(f"Error: {e}")

    finally:
        if ser.is_open:
            ser.close()

# Replace 'COM1' with your actual serial port name
receive_serial_data('COM5')
