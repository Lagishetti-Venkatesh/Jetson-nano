import cv2
print(cv2.__version__)

dispW = 320
dispH = 240
flip = 2
#camSet ='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(cv2.CAP_GSTREAMER)
while True:
    ret, frame = cam.read()
    frame = cv2.rectangle(frame, (340, 100), (450,190 ),(0, 255,0), -1)
    cv2.imshow('piCam', frame)
    cv2.moveWindow('piCam', 0,0) 
    if cv2.waitKey(1) == ord('q'):
        break 
cam.release()
cv2.destroyAllWindows()
