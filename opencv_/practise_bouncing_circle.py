import cv2

dispW = 640
dispH = 480
flip = 2

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

dx = 10
dy = 10
r = 30
x = 600
y = 400
while True:
    x = x+dx
    y = y+dy
    ret, frame = cam.read()
    cv2.circle(frame, (x, y), r, (0, 255, 0), -1 )
    font = cv2.FONT_HERSHEY_DUPLEX

    frame = cv2.putText(frame, 'Live Animation with Opencv', (50, 100), font, 1, (255, 0, 150), 3)
    cv2.imshow('picam', frame)
    cv2.moveWindow('picam', 50, 50)
    
    if x <=30 or x+r >= dispW:
        dx= dx*(-1)
    if y <=30 or y+r > dispH:
        dy = dy*(-1) 
    
   
    if cv2.waitKey(1)== ord('q'):
        break
cam.release()
cv2.destroyAllWindows()