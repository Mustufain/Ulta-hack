
import cv2
import numpy
import time
import playsound

class Hand_analyzer:
    
    
    def __init__(self):
        
        self.dirt_threshold = 35 #40 #40
        self.beep_thres     = 1000 #2100000 #2000000 #7000000#30000000 #30000000000000000000000000 #30000000

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
    
        print(red_pixels)
    
        if red_pixels > self.beep_thres: 

            #current_time = time.time()
            #if current_time > self.start_time + 1: 
            #    playsound.playsound('haha.mp3', 0)
            #    self.start_time = current_time
         
         
            return (filtered, True)   
        
        else:
            
            return (filtered, False)
              
            #bg_bad[150: 150 + 240, 
            #       100: 100 + 320, :]           = img_BGRA[ymin:ymax:ystep, xmin:xmax:xstep, :]
            
            #bg_bad[150: 150 + ymax/ystep,
            #       600: 600 + xmax/ystep, :]    = frame2[ymin:ymax:ystep, 
            #                                             xmin:xmax:xstep, :]
        
            #cv2.imshow('frame 2', frame2)
        
            #cv2.imshow('bg', bg_bad)
        
    #else:
        
        #bg_ok[150: 150 + 240, 
        #       100: 100 + 320, :]       = img_BGRA[ymin:ymax:ystep, xmin:xmax:xstep, :]
        
        #bg_ok[150: 150 + ymax/ystep,
        #       600: 600 + xmax/ystep, :]    = frame2[ymin:ymax:ystep, 
        #                                             xmin:xmax:xstep, :]
    
        #cv2.imshow('frame 2', frame2)
    
        #cv2.imshow('bg', bg_ok)
        
        
        
        
        
        
        