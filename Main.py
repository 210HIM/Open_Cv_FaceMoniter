import cv2 as cv
cap = cv.VideoCapture(0)

frame_width = int(cap.get(3)) 
frame_height = int(cap.get(4))

size = (frame_width, frame_height) 
result = cv.VideoWriter('filename.avi', cv.VideoWriter_fourcc(*'MJPG'), 10, size) 
while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break


cap.release()
cv.destroyAllWindows()