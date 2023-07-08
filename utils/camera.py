import cv2
import logging
import numpy as np

logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(name)s :: %(levelname)-8s :: %(message)s (%(filename)s:%(lineno)d)')
logger = logging.getLogger(__name__)

cap = None

def setup_env() -> None:
    global cap
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)
    logger.info('Camera environment setup complete')

def capture_img() -> np.ndarray:
    global cap
    ret, img = cap.read()
    if not ret:
        raise Exception('Camera not working')
    return img