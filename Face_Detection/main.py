# References the OpenCV (Open Source Computer Vision Library) module which is used for computer vision, image processing, and video analysis
import cv2

# Referencing the file that detects faces "haarcascade_frontalface_default.xml". Do not modify the xml file.
detect = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# Opens the desired image
imp_img = cv2.VideoCapture("D:\\Face_Detection\\trump.jpg")

res, img = imp_img.read()

# Converts image to black and white for better facial detection
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = detect.detectMultiScale(gray, 1.3, 5)
# Drawing a square on image
for (x, y, w, h) in faces:
    # Rectanlge format: (image, pt1, pt2, color, thickness)
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)

# Displays and closes the specified image
cv2.imshow("Trump", img)
cv2.waitKey(0)
imp_img.release()
cv2.destroyAllWindows()
