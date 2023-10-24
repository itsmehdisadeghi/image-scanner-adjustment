
import cv2
import numpy as np

wth = 255
hth = 320
img = cv2.imread("v.jpg")
points1= np.float32([[452 , 61] , [621, 54] , [500 , 334] ,[668, 307]])
points2 = np.float32([[0, 0] , [wth , 0] , [0 , hth] ,[wth, hth]])
matrix =  cv2.getPerspectiveTransform(points1, points2)
imgout = cv2.warpPerspective(img , matrix , (wth , hth))
cv2.imshow("out" , img)
cv2.imshow("outim" , imgout)
cv2.waitKey(0)

