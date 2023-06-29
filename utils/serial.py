import logging
import serial
from time import sleep

logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(name)s :: %(levelname)-8s :: %(message)s (%(filename)s:%(lineno)d)')
logger = logging.getLogger(__name__)

ser = None

def setup_env():
    global ser
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
    logger.info('Serial environment setup complete')

def send_trigger():
    ser.write(b't 1\n')
    sleep(0.01)
    logger.info('Trigger sent')
    
def send_set_led(index):
    ser.write('l {}\n'.format(index).encode('ascii'))
    sleep(0.01)
    logger.info('LED {} set'.format(index))