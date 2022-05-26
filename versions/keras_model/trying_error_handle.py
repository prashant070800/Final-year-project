import cv2
from mtcnn.mtcnn import MTCNN
detector = MTCNN()
cap = cv2.VideoCapture(0)
while True: 
    #Capture frame-by-frame
    __, frame = cap.read()
    
    #Use MTCNN to detect faces
    results = detector.detect_faces(frame)
    if results != []:
        for person in results:
            bounding_box = person['box']
            keypoints = person['keypoints']
            x1, y1, width, height = person['box']
    
            cv2.rectangle(frame,
                          (bounding_box[0], bounding_box[1]),
                          (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
                          (0,155,255),
                          2)
    
            
    #display resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) &0xFF == ord('q'):
        break
#When everything's done, release capture
cap.release()
cv2.destroyAllWindows()