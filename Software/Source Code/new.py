# coding: utf-8

# --------------------------------------------------------
# Object Detection in Video with Faster R-CNN
# Written by Masahiro Rikiso @ 2016/7/20
# --------------------------------------------------------


### Config

INPUT_FILE = r"C:\Users\Hp\OneDrive\Desktop\github\Final-year-project\Software\Source Code\WIN_20211203_20_45_04_Pro.mp4"
OUTPUT_FILE = r"C:\Users\Hp\OneDrive\Desktop\github\Final-year-project\Software\Source Code\output_Pro.mp4"
CONF_THRESH = 0.1
NMS_THRESH = 0.001


### Set Up Paths for Fast R-CNN
import os
import sys
# Add caffe to PYTHONPATH
caffe_path = os.path.join('/home','px','docker','py-faster-rcnn', 'caffe-fast-rcnn', 'python')
sys.path.insert(0, caffe_path)
# Add lib to PYTHONPATH
lib_path = os.path.join('/home','px','docker','py-faster-rcnn', 'lib')
sys.path.insert(0, lib_path)


### Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2
import caffe
from fast_rcnn.config import cfg
from fast_rcnn.test import im_detect
from fast_rcnn.nms_wrapper import nms


### Define Object-Detection-Function
CLASSES = ('__background__',
           'aeroplane', 'bicycle', 'bird', 'boat',
           'bottle', 'bus', 'car', 'cat', 'chair',
           'cow', 'diningtable', 'dog', 'horse',
           'motorbike', 'person', 'pottedplant',
           'sheep', 'sofa', 'train', 'tvmonitor')

NETS = {'vgg16': ('VGG16',
                  'VGG16_faster_rcnn_final.caffemodel'),
        'zf': ('ZF',
                  'ZF_faster_rcnn_final.caffemodel')}

def obj_detect(net, im):
    """Detect object classes in an image using pre-computed object proposals."""

    # Detect all object classes and regress object bounds
    scores, boxes = im_detect(net, im)
    #im = im[:, :, (2, 1, 0)]
    # Visualize detections for each class
    for cls_ind, cls in enumerate(CLASSES[1:]):
        if cls is "bicycle"  or cls is "bus" or cls is "car" or cls is "motorbike" or cls is "person":
            cls_ind += 1 # because we skipped background
            cls_boxes = boxes[:, 4*cls_ind:4*(cls_ind + 1)]
            cls_scores = scores[:, cls_ind]
            dets = np.hstack((cls_boxes, cls_scores[:, np.newaxis])).astype(np.float32)
            keep = nms(dets, NMS_THRESH)
            dets = dets[keep, :]
            im = vis_detections(str(cls_ind), im, cls, dets, thresh=CONF_THRESH)
    return im

def vis_detections(image_name, im, class_name, dets, thresh=0.5):
    """Draw detected bounding boxes."""
    inds = np.where(dets[:, -1] >= thresh)[0]
    if len(inds) == 0:
        return im

    for i in inds:
        bbox = dets[i, :4]
        score = dets[i, -1]

        if (bbox[2] - bbox[0]) < 352 and (bbox[3] - bbox[1]) < 240:
            cv2.putText(im, '{:s} {:.3f}'.format(class_name, score),(int(bbox[0]),int(bbox[1]) - 2), cv2.FONT_HERSHEY_SIMPLEX, 0.8,(255,0,0),2)
            cv2.rectangle(im,(bbox[0], bbox[1]),(bbox[2],bbox[3]),(100,255,100),3)        
    return im


### Load Video
cap = cv2.VideoCapture(INPUT_FILE)

width = cap.get(3)
height = cap.get(4)
fps = cap.get(5)
count = cap.get(7)
framspan = 1./fps


### Load Faster-R-CNN Model
cfg.TEST.HAS_RPN = True  # Use RPN for proposals
prototxt = os.path.join(cfg.MODELS_DIR, NETS['vgg16'][0],
                            'faster_rcnn_alt_opt', 'faster_rcnn_test.pt')
caffemodel = os.path.join(cfg.DATA_DIR, 'faster_rcnn_models',
                              NETS['vgg16'][1])

caffe.set_mode_gpu()
caffe.set_device(0)
cfg.GPU_ID = 0
net = caffe.Net(prototxt, caffemodel, caffe.TEST)


### Detect Object ! !
fourcc = cv2.cv.CV_FOURCC('M','P','4','2')
out = cv2.VideoWriter(OUTPUT_FILE, fourcc, fps, (int(width),int(height)), 1)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = obj_detect(net, frame)
        out.write(frame)
        
        #cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()