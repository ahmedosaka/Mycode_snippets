# # Canny Edge Detection
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('messi.jpg',0)
# edges = cv2.Canny(img,100,200)

# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# plt.show()


# Canny Edge Detection
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# cap  = cv2.VideoCapture(0)
# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     edges = cv2.Canny(frame,100,200)

#     plt.subplot(121),plt.imshow(frame,cmap = 'gray')
#     plt.title('Original Image'), plt.xticks([]), plt.yticks([])
#     plt.subplot(122),plt.imshow(edges,cmap = 'gray')
#     plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    
#     plt.show()
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()

# import cv2


# def canny_webcam():
#     "Live capture frames from webcam and show the canny edge image of the captured frames."

#     cap = cv2.VideoCapture(0)

#     while True:
#         ret, frame = cap.read()  # ret gets a boolean value. True if reading is successful (I think). frame is an
#         # uint8 numpy.ndarray

#         frame = cv2.GaussianBlur(frame, (7, 7), 1.41)
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         edge = cv2.Canny(frame, 25, 75)

#         cv2.imshow('Canny Edge', edge)

#         if cv2.waitKey(20) == ord('q'):  # Introduce 20 milisecond delay. press q to exit.
#             break

# canny_webcam()


# Hand Detection and Finger Counting Using OpenCV-Python
# import numpy as np
# import cv2 as cv

# def skinmask(img):
#     hsvim = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#     lower = np.array([0, 48, 80], dtype = "uint8")
#     upper = np.array([20, 255, 255], dtype = "uint8")
#     skinRegionHSV = cv.inRange(hsvim, lower, upper)
#     blurred = cv.blur(skinRegionHSV, (2,2))
#     ret, thresh = cv.threshold(blurred,0,255,cv.THRESH_BINARY)
#     return thresh

# def getcnthull(mask_img):
#     contours, hierarchy = cv.findContours(mask_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#     contours = max(contours, key=lambda x: cv.contourArea(x))
#     hull = cv.convexHull(contours)
#     return contours, hull

# def getdefects(contours):
#     hull = cv.convexHull(contours, returnPoints=False)
#     defects = cv.convexityDefects(contours, hull)
#     return defects

# cap = cv.VideoCapture(0) # '0' for webcam
# while cap.isOpened():
#     _, img = cap.read()
#     try:
#         mask_img = skinmask(img)
#         contours, hull = getcnthull(mask_img)
#         cv.drawContours(img, [contours], -1, (255,255,0), 2)
#         cv.drawContours(img, [hull], -1, (0, 255, 255), 2)
#         defects = getdefects(contours)
#         if defects is not None:
#             cnt = 0
#             for i in range(defects.shape[0]):  # calculate the angle
#                 s, e, f, d = defects[i][0]
#                 start = tuple(contours[s][0])
#                 end = tuple(contours[e][0])
#                 far = tuple(contours[f][0])
#                 a = np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
#                 b = np.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
#                 c = np.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
#                 angle = np.arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  #      cosine theorem
#                 if angle <= np.pi / 2:  # angle less than 90 degree, treat as fingers
#                     cnt += 1
#                     cv.circle(img, far, 4, [0, 0, 255], -1)
#             if cnt > 0:
#                 cnt = cnt+1
#             cv.putText(img, str(cnt), (0, 50), cv.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0) , 2, cv.LINE_AA)
#         cv.imshow("img", img)
#     except:
#         pass
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv.destroyAllWindows()

