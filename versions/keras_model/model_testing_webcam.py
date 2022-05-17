from face_detection_webcam import extract_face
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
#from keras_facenet import FaceNet
import warnings
warnings.filterwarnings('ignore')

label = ["Ajeet", "Maneesh", "Pranjal", "Raj"]
model = load_model(r"C:\Users\Hp\OneDrive\Desktop\github\Final-year-project\versions\keras_model\Testing_keras.h5")
img_counter = 0

cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    if not ret:
        print('failed to grab frame')
        break
    cv2.imshow("frame", frame)
    valx = extract_face(frame)
    cv2.imshow("valx", valx)
    valx = np.array(valx)
    valx = valx.reshape((1, 160, 160, 3))
    print(valx.shape)

    pred = model.predict(valx)
    print(pred)
    print(label[np.argmax(pred)])
    #to get continuous live video feed from my laptops webcam
    k  = cv2.waitKey(1)
    # if the escape key is been pressed, the app will stop
    if k%256 == 27:
        print('escape hit, closing the app')
        break
    # if the spacebar key is been pressed
    # screenshots will be taken
    elif k%256  == 32:
        # the format for storing the images scrreenshotted
        img_name = f'opencv_frame_{img_counter}'
        # saves the image as a png file
        cv2.imwrite(img_name, frame)
        print('screenshot taken')
        # the number of images automaticallly increases by 1
        img_counter += 1

# release the camera
cam.release()

# stops the camera window
cam.destoryAllWindows()
