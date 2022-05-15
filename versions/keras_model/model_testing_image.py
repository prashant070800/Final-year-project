from face_detection import extract_face
from Embedding import get_embedding
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
#from keras_facenet import FaceNet
import warnings
warnings.filterwarnings('ignore')

label = ["Ajeet", "Maneesh", "Pranjal", "Raj"]



t = r"C:\Users\ajeet\AppData\Local\Programs\Python\Python310\Finalize\face_dataset\val\RAJ\image81.jpg"
valx = extract_face(t)
#print(valx.shape)
cv2.imshow("valx", valx)
#import matplotlib.pyplot as plt
#cv2.imshow('Main image',z) 
#cv2.imshow('pixel1', pixel)

valx = np.array(valx)
valx = valx.reshape((1, 160, 160, 3))
print(valx.shape)
model = load_model(r"C:\Users\ajeet\AppData\Local\Programs\Python\Python310\Finalize\Testing_keras.h5")
pred = model.predict(valx)
print(pred)
print(label[np.argmax(pred)])
#print(yhat[0].type())
