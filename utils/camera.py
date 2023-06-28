import cv2
import logging

logging.basicConfig(level=logging.INFO, format='%(name)s :: %(levelname)-8s :: %(message)s')
logger = logging.getLogger(__name__)

cap = None

def setup_env():
    global cap
    cap = cv2.VideoCapture(0)
    logger.info('Camera environment setup complete')

def capture_img():
    global cap
    ret, img = cap.read()
    if not ret:
        raise Exception('Camera not working')
    return img