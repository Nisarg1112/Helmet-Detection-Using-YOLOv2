import cv2
from darkflow.net.build import TFNet
import numpy as np
import time

options = {
    'model': 'cfg/yolov2-tiny.cfg',
    'load': 'bin/yolov2-tiny_3000.weights',
    'threshold': 0.1,
}

tfnet = TFNet(options)
colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]

frame = cv2.imread('img.jpg') # Here img.jpg is image name Or you can also give the path with extension of the file like jpg,jpeg,png etc
results = tfnet.return_predict(frame)
for color, result in zip(colors, results):
    tl = (result['topleft']['x'], result['topleft']['y'])
    br = (result['bottomright']['x'], result['bottomright']['y'])
    label = result['label']
    confidence = result['confidence']
    text = '{}: {:.0f}%'.format(label, confidence * 100)
    frame = cv2.rectangle(frame, tl, br, color, 3)
    frame = cv2.putText(frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
cv2.imshow('aa', frame)
cv2.waitKey(0)