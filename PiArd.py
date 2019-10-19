import serial
import time

ser = serial.Serial('/dev/ttyACM0',9600)
# ser.open()
ser.write(b'5')
time.sleep(2)
ser.write(b'2')
time.sleep(2)
ser.write(b'20')
time.sleep(2)


print("Name: " + ser.name)
if ser.is_open:
    print("open")
else:
    print("closed")

for item in ser.get_settings():
    print("Settings: " + item)

# python -m serial.tools.list_ports
# python -m serial.tools.miniterm <port_name> #use option -h to get a listing of all options)

ser.close()
# while 1:
#     print(ser.readline())

with serial.Serial('/dev/ttyACM0', 9600, timeout=1) as ser:
    print(ser.read())          # read one byte
    print(ser.read(10) )       # read up to ten bytes (timeout)
    print(ser.readline())   # read a '\n' terminated line
