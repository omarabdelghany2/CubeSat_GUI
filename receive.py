import serial

# Change the port to the correct one for your Arduino Uno
port = "COM3"  # Update with your Arduino's port

# Open the serial connection
ser = serial.Serial(port, 115200, timeout=1000)

try:
    # Read a line from the serial port
    line = ser.readline().decode("utf-8").strip()
    print(line)
except KeyboardInterrupt:
    # Close the serial connection when the script is interrupted
    ser.close()
