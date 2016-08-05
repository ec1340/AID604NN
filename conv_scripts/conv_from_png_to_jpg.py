
# coding: utf-8

# In[2]:

from PIL import Image
import os
import fnmatch


# In[3]:

print("converting from png to jpg")


# In[4]:

count = 0


# In[ ]:

for file in os.listdir('.'):
    num_of_files = len([name for name in os.listdir('.')]) 
    if fnmatch.fnmatch(file, '*.png'):
        img = Image.open(file)
        file_name = str(file)
        file_name_CID = file_name[:-4]
        img.save(str(file_name_CID) + '.jpg')
        count = count + 1
        print('converting pic ' + str(count) + " out of " + str(num_of_files))
    

