import numpy as np                                              
import cv2                                                      

def nothing(x):                                                 
     pass

cv2.namedWindow('BGR', cv2.WINDOW_NORMAL)                        
cv2.createTrackbar('Blue', 'BGR', 0, 255, nothing)                  
cv2.createTrackbar('Green', 'BGR', 0, 255, nothing)                 
cv2.createTrackbar('Red', 'BGR', 0, 255, nothing)

bgr=np.ones((480, 720, 3), np.uint8)

while True :
     
     k = cv2.waitKey(1) & 0xFF                               
     if k == 27:
          break
     
     b = cv2.getTrackbarPos('Blue', 'BGR')                         
     g = cv2.getTrackbarPos('Green', 'BGR')                       
     r = cv2.getTrackbarPos('Red', 'BGR')
     
     bgr[:]=[b, g, r]
     cv2.imshow('BGR', bgr)
    
cv2.destroyAllWindows()                           
