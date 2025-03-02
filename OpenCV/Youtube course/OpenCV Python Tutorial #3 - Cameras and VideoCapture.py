import numpy as np 
import cv2

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	width = int(cap.get(3))
	height = int(cap.get(4))

	image = np.zeros(frame.shape, np.uint8)
	smaller_frame = cv2.resize(frame,(0,0), fx=0.5,fy=0.5)
	image[:height//2,:width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180) #top_left
	image[height//2:,:width//2] = smaller_frame #bottom_left
	image[:height//2,width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180) #top_right
	image[height//2:,width//2:] = smaller_frame #bottom_right


	cv2.imshow('frame', image)
	
	if cv2.waitKey(100) == ord('q'):
		break

cap.release()
cv2.destryAllWindows()
