import app
import cv2
import os

class Logic:
    def getImg():
        return
    
    def img_process(imgPath):
        image = cv2.imread("/image/"+imgPath)
        imageSize = cv2.resize(image,(700,700))
        
        cv2.imshow("Size", imageSize)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
       
    