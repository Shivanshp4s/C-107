import cv2 

video = cv2.VideoCapture("C:/Users/DELL/Documents/python/Obejct detection and traking c106/bb3.mp4")

#load the tracker
tracker = cv2.TrackerCSRT_create()

#read the first frame of the video 
returned,img = video.read()

#seclect the bounding box on the make
bbox = cv2.selectROI("tracking",img,False)

#insialise the tracker on img and bounding box
tracker.init(img,bbox)

print(bbox)

"""while True:
    check,img = video.read()

    cv2.imshow("frame",img)

    if cv2.waitKey(0) == 32:
        print("stopped")
        break
"""
video.release()
cv2.destroyAllWindows()