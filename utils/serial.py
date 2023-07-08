import logging
import serial
from time import sleep

logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(name)s :: %(levelname)-8s :: %(message)s (%(filename)s:%(lineno)d)')
logger = logging.getLogger(__name__)

ser = None

def setup_env(device_name: str) -> None:
    global ser
    ser = serial.Serial(device_name, 115200, timeout=1)
    for i in range(4):
        ser.write('l {} 0\r\n'.format(i).encode('ascii'))
    sleep(0.1)
    logger.info('Serial environment setup complete, connection to {} established'.format(device_name))

def set_servo(degree: int) -> None:
    ser.write('servo {}\r\n'.format(degree).encode('ascii'))
    sleep(0.1)
    logger.info('Servo set to {} degrees'.format(degree))
    
def set_led(index: int, state: bool) -> None:
    ser.write('l {} {}\r\n'.format(index, int(state)).encode('ascii'))
    sleep(0.1)
    logger.info('LED {} set to {}'.format(index, state))