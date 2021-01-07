import cv2
print(cv2.__version__)

dispW = 1280
dispH = 960
flip = 2
#camSet ='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam = cv2.VideoCapture(0)
cam = cv2.VideoCapture('videos/myvideo.avi' )

#vid2 = cv2.VideoWriter('videos/myvideo.avi', cv2.VideoWriter_fourcc(*'XVID'), 21, (640, 480))
while True:
    ret, frame = cam.read()
    
    cv2.imshow('piCam', frame)
    cv2.moveWindow('piCam', 0,0)
    #vid2.write(frame)
    if cv2.waitKey(50) == ord('q'):
        break 
cam.release()
#vid2.release()
cv2.destroyAllWindows()
