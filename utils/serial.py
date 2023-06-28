import logging
import serial

logging.basicConfig(level=logging.INFO, format='%(name)s :: %(levelname)-8s :: %(message)s')
logger = logging.getLogger(__name__)

ser = None

def setup_env():
    global ser
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    logger.info('Serial environment setup complete')

def send_trigger():
    ser.write(b'1')
    logger.info('Trigger sent')