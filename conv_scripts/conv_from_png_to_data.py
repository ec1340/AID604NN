
# coding: utf-8

# In[2]:


from PIL import Image
import os
import fnmatch
import numpy as np
import time


# In[3]:

print("start time: " + str(time.ctime()))
start = time.time()
print("converting images to csv....")
print("......")

csv_data = []
x = 0
for file in os.listdir('.'):
    num_of_files = len([name for name in os.listdir('.')]) 
    if fnmatch.fnmatch(file, '*.png'):
        pixel_data = Image.open(file)
        size = width, height = pixel_data.size
        out_data = np.asarray((list(pixel_data.getdata())))
        csv_data.append(out_data)
        x = x + 1
        print("on pic: " + str(x) + " out of " + str((num_of_files - 2)))


# In[4]:

print("finish time: " + str(time.ctime()))
end = time.time()
elapsed = end - start
print("elapsed time: " +str(elapsed)+ " seconds")


# In[5]:

filename = input("please enter the desired file name + .csv: ")
np.savetxt(filename, csv_data, delimiter=',')


# In[6]:

ar = np.asarray(csv_data)


# In[7]:

print("the output dataset's dimensions are " + str(ar.data.shape))


# In[ ]:



