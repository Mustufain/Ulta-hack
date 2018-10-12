

###############################3
# Note! put cameras to different usb hub (different side of the computer)
####################################



import numpy as np
import cv2

cap     = cv2.VideoCapture(1)
cap2    = cv2.VideoCapture(2) 

threshold = 40

while(True):
    # Capture frame-by-frame
    ret,    frame   = cap.read()
    ret2,   frame2  = cap2.read()


    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #color = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    b_channel, g_channel, r_channel = cv2.split(frame)

    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 50 #creating a dummy alpha channel image.

    img_BGRA = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))

    print(img_BGRA.shape)


    #img_BGRA[gray < 240, 3] = 0

    img_BGRA[gray > threshold, 0] = 0 #gray[gray < 200]
    img_BGRA[gray > threshold, 1] = 0 #gray[gray < 200]
    img_BGRA[gray > threshold, 2] = 255 #gray[gray < 200]
#    img_BGRA[gray < 240, 0] = gray[gray < 240]
    

    # Display the resulting frame
    #cv2.imshow('frame', gray)
    
    cv2.imshow('frame', img_BGRA)
    
    cv2.imshow('frame 2', frame2)
       
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

