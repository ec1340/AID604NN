
# coding: utf-8

# In[4]:

import PIL
from PIL import Image

import os
import fnmatch
import numpy as np
import time

print("start time: " + str(time.ctime()))
start = time.time()
print("converting images to greyscale and resizing to 100x100....")
print("......")

count = 0

for file in os.listdir('.'):
    num_of_files = len([name for name in os.listdir('.')]) 
    if fnmatch.fnmatch(file, '*.png'):
        x = Image.open(file, 'r')
        newsize = (50,50)
        x.thumbnail(newsize, PIL.Image.ANTIALIAS)
        x = x.convert('L')
        y = np.asarray(x.getdata(),dtype=np.float64).reshape((x.size[1],x.size[0]))
        y = np.asarray(y, dtype=np.uint8)
        w = Image.fromarray(y, mode='L')
        w.save(file)
        count = count + 1
        print("on pic: " + str(count) + " out of " + str((num_of_files - 2)))
        
        
print("finish time: " + str(time.ctime()))
end = time.time()
elapsed = end - start
print("elapsed time: " +str(elapsed)+ " seconds")


# In[ ]:



