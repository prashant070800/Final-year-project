# function for face detection with mtcnn
from PIL import Image
from numpy import asarray
from mtcnn.mtcnn import MTCNN
import cv2 
# extract a single face from a given photograph
def extract_face(filename, required_size=(160, 160)):
	# load image from file
	image = Image.open(filename)
	# convert to RGB, if needed
	image = image.convert('RGB')
	# convert to array
	pixels = asarray(image)
	# create the detector, using default weights
	detector = MTCNN()
	# detect faces in the image
	results = detector.detect_faces(pixels)
	# extract the bounding box from the first face
	x1, y1, width, height = results[0]['box']
	# bug fix
	x1, y1 = abs(x1), abs(y1)
	x2, y2 = x1 + width, y1 + height
	# extract the face
	face = pixels[y1:y2, x1:x2]
	# resize pixels to the model size
	image = Image.fromarray(face)
	image = image.resize(required_size)
	face_array = asarray(image)
	return face_array
 

#t = r"C:\Users\ajeet\AppData\Local\Programs\Python\Python310\Finalize\face_dataset\val\RAJ\image84.jpg"
#pixel = extract_face(t)
#print(pixel.shape)
#z = cv2.imread(t)
#import matplotlib.pyplot as plt
#cv2.imshow('Main image',z) 
#cv2.imshow('pixel1', pixel)
#cv2.imwrite('Cropped_raj.jpg',pixel)

