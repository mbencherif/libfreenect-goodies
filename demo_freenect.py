#!/usr/bin/env python
from freenect import sync_get_depth as get_depth, sync_get_rgb as get_rgb
import cv  
import numpy as np
  
def doloop():
    global depth, rgb
    while True:
        # Get a fresh frame
        depth, rgb = get_depth(), get_rgb()
        
        # Build a two panel color image
        d3 = np.dstack((depth,depth,depth)).astype(np.uint8)
        da = np.hstack((d3,rgb))
        
        # Simple Downsample
        cv.ShowImage('both',array2cv(da[::2,::2,::-1]))
        cv.WaitKey(5)
        
doloop()

"""
IPython usage:
 ipython
 [1]: run -i demo_freenect
 #<ctrl -c>  (to interrupt the loop)
 [2]: %timeit -n100 get_depth(), get_rgb() # profile the kinect capture

"""

