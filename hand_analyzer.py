
#####################################
# Hand Analyzer                     #
#####################################
#
# This file analyzes the cleanliness
# of the hands
#
#####################################

# import libraries
import cv2
import numpy
import time
import playsound

class Hand_analyzer:
    
    def __init__(self):
    
        # set parameters for dirt and beep (if enabled)
        self.dirt_threshold = 35 
        self.beep_thres     = 1000

        self.bg_ok       = cv2.imread('software_image_ok.png',1)
        self.bg_bad      = cv2.imread('software_image_bad.png',1) 

        self.xmin   = 0
        self.ymin   = 0
        self.ymax   = 480
        self.xmax   = 640
        self.xstep  = 2
        self.ystep  = 2

        self.start_time = 0

    def is_dirty(self, filtered):
           
        
        # threshold the dirty pixels
        gray = cv2.cvtColor(filtered, cv2.COLOR_BGR2GRAY)

        filtered[gray > self.dirt_threshold, 0] = 0 #gray[gray < 200]
        filtered[gray > self.dirt_threshold, 1] = 0 #gray[gray < 200]
        filtered[gray > self.dirt_threshold, 2] = 255 #gray[gray < 200]
        filtered[gray < self.dirt_threshold, 2] = 0
    
        red_pixels = numpy.sum(filtered[50:,:,2])
    
        # if threshold is exceeded return thresholded image and set is_dirty flag to True
        if red_pixels > self.beep_thres: 
            
            # uncomment these lines if you want a beep
            #current_time = time.time()
            #if current_time > self.start_time + 1: 
            #    playsound.playsound('haha.mp3', 0)
            #    self.start_time = current_time
      
            return (filtered, True)   
        
        # if threshold is not exceeded, return thresholded image and set is_dirty flag to False
        else:
            
            return (filtered, False)
           
        
