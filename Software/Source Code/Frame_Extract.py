import os
from time import sleep
import cv2

# Read the video from specified path
cam = cv2.VideoCapture(0)

try:

    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0

while currentframe < 10:

    # reading from frame
    ret, frame = cam.read()

    if ret:
        # if video is still left continue creating images
        name = './data/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)

        # writing the extracted images
        cv2.imshow(name, frame)
        cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
        sleep(1)

    else:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()