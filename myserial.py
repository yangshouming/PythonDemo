import serial
import serial.tools.list_ports

sPort = 'COM1'
sBaudRate = 9600
sTimeOut = 1

# port_list = list(serial.tools.list_ports.comports())
# if len(port_list) == 0:
#     print('找不到串口')
# else:
#     for i in range(0, len(port_list)):
#         print(port_list[i])

# str_com = port_list[1]
# str_com = str(str_com)
# sPort = (str_com[0:5])
sPort.strip()

# sPort = 'COM3'

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


# print(myserial.read(6))
