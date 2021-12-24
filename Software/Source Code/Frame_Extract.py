import os
from time import sleep
import cv2

# Read the video from specified path
cam = cv2.VideoCapture(r"C:\Users\Hp\OneDrive\Desktop\github\Final-year-project\Software\Source Code\maneesh.mp4")

try:

    # creating a folder named data
    if not os.path.exists('image'):
        os.makedirs('image')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0

while currentframe < 1500:

    # reading from frame
    ret, frame = cam.read()

    if ret:
        # if video is still left continue creating images
        name = './image/image' + str(currentframe//15) + '.jpg'
        print('Creating...' + name)

        # writing the extracted images # At this stage I am saving data also to manage database 
        #cv2.imshow(name, frame)
        cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 15
        cam.set(cv2.CAP_PROP_POS_FRAMES, currentframe)
        

    else:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
