import cv2
dispW = 720
dispH = 640
print(cv2.__version__)

cam = cv2.VideoCapture(0)
record = cv2.VideoWriter('videos/result.mp4', cv2.VideoWriter_fourcc(*'XVID'), 21, (dispW, dispH))
while True:
    ret , frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Frame with Gray color', gray)
    cv2.imshow('Frame_received_Through camera', frame)
    cv2.moveWindow('Frame_received_Through camera', 700, 0)
    frameS = cv2.resize(frame, (320, 240))
    cv2.imshow('Small frame',frameS )
    cv2.moveWindow('Frame with Gray color', 0, 0)
    record.write(frame)

    if cv2.waitKey(1)== ord('q'):
        break
    
cam.release()
record.release()
cv2.destroyAllWindows()