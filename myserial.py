import serial

sPort = 'COM37'
sBaudRate = 115200
sTimeOut = 1
try:
    myserial = serial.Serial(port=sPort, baudrate=sBaudRate, timeout=sTimeOut)
    print('open serial ok')
except:
    print('open serial error')

try:
    serial_read_data = myserial.readline()
    print(serial_read_data)
    # snum = int(serial_read_data)
    # print(snum)

except:
    print('serial_read_data error')


print(myserial.read(6))
