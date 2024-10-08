import serial
import time

# Replace 'COM3' with your Arduino's COM port
ser = serial.Serial('COM3', 9600)  # Adjust 'COM3' to match your Arduino's COM port
time.sleep(2)  # Wait for the serial connection to initialize

# Data to send (example: binary '110', which is 6 in decimal)
data = 0b110  # You can replace this with the actual binary data you want to send

# Send the binary data as a single byte
ser.write(bytes([data]))

# Close the serial connection
ser.close()
