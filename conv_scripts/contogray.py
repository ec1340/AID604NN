
# coding: utf-8

# In[1]:

from PIL import Image 
import os
import fnmatch
import numpy as np




# In[15]:

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.png'):
        x = Image.open(file, 'r')
        x = x.convert('L')
        y = np.asarray(x.getdata(),dtype=np.float64).reshape((x.size[1],x.size[0]))
        y = np.asarray(y, dtype=np.uint8)
        w = Image.fromarray(y, mode='L')
        w.save(file)

