import logging
import serial
from time import sleep

logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(name)s :: %(levelname)-8s :: %(message)s (%(filename)s:%(lineno)d)')
logger = logging.getLogger(__name__)

ser = None

def setup_env() -> None:
    global ser
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
    for i in range(4):
        ser.write('l {} 0\r\n'.format(i).encode('ascii'))
    sleep(0.1)
    ser.write(b'servo 0\r\n')
    logger.info('Serial environment setup complete')

def send_trigger() -> None:
    ser.write(b'servo 180\r\n')
    sleep(0.1)
    logger.info('Trigger sent')
    
def set_led(index: int, state: bool) -> None:
    ser.write('l {} {}\r\n'.format(index, int(state)).encode('ascii'))
    sleep(0.1)
    logger.info('LED {} set to {}'.format(index, state))