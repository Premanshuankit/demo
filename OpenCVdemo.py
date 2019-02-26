import cv2
 
image = cv2.imread("C:\\Users\\Premanshu Ankit\\Desktop\\download.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Over the Clouds", image)
cv2.imshow("Over the Clouds - gray width 4000px", gray_image)
# cv2.SetCaptureProperty(cam,cv.CV_CAP_PROP_FRAME_WIDTH,1920)
# cv2.SetCaptureProperty(cam,cv.CV_CAP_PROP_FRAME_WIDTH,1080)
cv2.waitKey(0)
cv2.destroyAllWindows()