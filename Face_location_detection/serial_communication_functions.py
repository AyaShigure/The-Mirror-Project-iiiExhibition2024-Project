import serial
import time 
import os

class arduino_control():
    def __init__(self, serial_port):
        try:
            self.arduino = serial.Serial(port=serial_port, baudrate=115200, timeout=.1) 
        except:
            print('Invalid port, exiting..')
            os.exit(0)
    def check_connection(self):
        pass

    def send_control_to_arduino(self, send_data):
        _ = self.arduino.readline()
        send_data = str(send_data) + 'a'
        self.arduino.write(bytes(send_data, 'utf-8')) #  THETA_Y_DATA = 0
        time.sleep(0.05)
        arduino_status = self.arduino.readline()
        # string = "b''"
        # if arduino_status == bytes(string, 'utf-8'):
        #     print('THERE IS NO DATA SENT BACK')
        # print(type(float(arduino_status)))
        print(f'[MacOS : Reading from the serial port]: {arduino_status}')

        # self.arduino.write(bytes(str(theta_y), 'utf-8')) 
        # time.sleep(0.05)
        # # arduino.write(bytes(theta_z, 'utf-8')) 
        # arduino_status = self.arduino.readline()
        # time.sleep(0.05)
        # arduino_status = self.arduino.readline()
        # time.sleep(0.05)
        # print(f'[MacOS : Reading from the serial port]: {arduino_status}')
        # if arduino_status == 'ok':
        #     print('Arduino status: GREEN')
        # else:
        #     print('Communication with arduion failed, exiting..')
        #     os.exit(0)
    def close_port(self):
        self.arduino.close()


port = '/dev/cu.usbserial-00000000'
arduino = arduino_control(port)

arduino.check_connection()

theta_y = 2.0
theta_z = 3.0
for i in range(20):
    time.sleep(1)
    arduino.send_control_to_arduino(10.1)
arduino.close_port()
# while()

