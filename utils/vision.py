import logging
import argparse
from pathlib import Path
import random

import cv2
import numpy as np

from utils.model_utils import blob, det_postprocess, letterbox, path_to_list
from utils.pycuda_api import TRTEngine

Engine = None
Engine_H = None
Engine_W = None

# Enable Logging
logging.basicConfig(level=logging.INFO, format='%(name)s :: %(levelname)-8s :: %(message)s')
logger = logging.getLogger(__name__)

# Model Configuration
CLASSES = ('china', 'indonesia', 'pirate')
COLORS = {
    cls: [random.randint(0, 255) for _ in range(3)]
    for i, cls in enumerate(CLASSES)
}

def setup_env():
    global Engine, Engine_H, Engine_W
    Engine = TRTEngine("model/yolov8.engine")
    Engine_H, Engine_W = Engine.inp_info[0].shape[-2:]
    logger.info('Vision environment setup complete')

def detect_flag(img: np.array):
    bgr_img, ratio, dwdh = letterbox(img, (Engine_W, Engine_H))
    rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
    tensor = blob(rgb_img, return_seg=False)
    dwdh = np.array(dwdh * 2, dtype=np.float32)
    tensor = np.ascontiguousarray(tensor)
    data = Engine(tensor)
    bboxes, scores, labels = det_postprocess(data)
    bboxes -= dwdh
    bboxes /= ratio
    return (bboxes, scores, labels)

def visualization(img: np.array, bboxes: np.array, scores: np.array, labels: np.array):
    draw = img.copy()
    for (bbox, score, label) in zip(bboxes, scores, labels):
        bbox = bbox.round().astype(np.int32).tolist()
        cls_id = int(label)
        cls = CLASSES[cls_id]
        color = COLORS[cls]
        cv2.rectangle(draw, (bbox[0], bbox[1]), (bbox[2], bbox[3]), color, 2)
        cv2.putText(draw,
                    f'{cls}:{score:.3f}', (bbox[0], bbox[1] - 2),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.75, [225, 255, 255],
                    thickness=2)
    cv2.imshow('frame', draw)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return True
    else:
        return False