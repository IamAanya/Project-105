import cv2
vid=cv2.VideoCapture(0)
if(vid.isOpened()==False):
    print("Unable to read the feed")
while True:
    ret,frame=vid.read()
    cv2.imshow("webcam",frame)
    if cv2.waitKey(25)==32:
        break
vid.release()
cv2.destroyAllWindows()        