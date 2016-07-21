
# coding: utf-8

# In[1]:

#import needed libraries
import fnmatch
import os
import pickle
import pprint
import shutil


# In[8]:

#load pickled list of active compounds not found in batch_1
compound_list = pickle.load( open("list_of_active_cmps_158.p", "rb"))


# In[9]:

[int(x) for x in compound_list] # converts the ID's to int


# In[ ]:

#set destination
print("the current working directory is: " + str(os.getcwd()))
dest = input("enter destination: ")

#iterate through directory and move file up to destination 
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.png'):  #possible origin of bug
        file_name = str(file)
        file_name = file_name[:-4]
        for x in range(0,len(compound_list)):
            xref = compound_list[x]
            if int(xref) == int(file_name):
                shutil.copy(file, dest)
    

