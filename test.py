import cv2 as cv
vid = cv.VideoCapture("filename.avi")
while True:
    rat,fream = vid.read()
    cv.imshow("fream", fream)
    if cv.waitKey(1) & 0xFF == ord('q'): 
        break
cv.destroyAllWindows() 