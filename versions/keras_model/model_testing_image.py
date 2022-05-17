from face_detection import extract_face
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
#from keras_facenet import FaceNet
import warnings
warnings.filterwarnings('ignore')

label = ["Ajeet", "Maneesh", "Pranjal", "Raj"]



t = r"C:\Users\Hp\OneDrive\Desktop\github\Final-year-project\images\image\image2.jpg"
valx = extract_face(t)
#print(valx.shape)
cv2.imshow("valx", valx)
#import matplotlib.pyplot as plt
#cv2.imshow('Main image',z) 
#cv2.imshow('pixel1', pixel)

valx = np.array(valx)
valx = valx.reshape((1, 160, 160, 3))
print(valx.shape)
model = load_model(r"C:\Users\Hp\OneDrive\Desktop\github\Final-year-project\versions\keras_model\Testing_keras.h5")
pred = model.predict(valx)
print(pred)
print(label[np.argmax(pred)])
#print(yhat[0].type())
