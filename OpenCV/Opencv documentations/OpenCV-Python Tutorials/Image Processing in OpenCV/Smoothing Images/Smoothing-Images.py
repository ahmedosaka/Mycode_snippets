# # 2D Convolution ( Image Filtering )

# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('opencv_logo.png')

# kernel = np.ones((5,5),np.float32)/25
# dst = cv2.filter2D(img,-1,kernel)

# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
# plt.xticks([]), plt.yticks([])
# plt.show()


# Image Blurring (Image Smoothing)
# 1. Averaging
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('opencv_logo.png')

# blur = cv2.blur(img,(5,5))

# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
# plt.xticks([]), plt.yticks([])
# plt.show()

# 2. Gaussian Filtering

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencv_logo.png')

blur = cv2.GaussianBlur(img,(5,5),0)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()



# 3. Median Filtering

# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('Text_bef.jpg')
# median = cv2.medianBlur(img,5)
# blur = cv2.GaussianBlur(median,(5,5),0)


# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(median),plt.title('Blurred')
# plt.xticks([]), plt.yticks([])
# plt.show()


# 4. Bilateral Filtering

# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('Text_bef.jpg')
# blur = cv2.bilateralFilter(img,100,75,75)



# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
# plt.xticks([]), plt.yticks([])
# plt.show()


