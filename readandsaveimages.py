#!/usr/bin/env python
# coding: utf-8

# In[108]:


import os
get_ipython().system('pip install --upgrade pip')
get_ipython().system('pip install pandas')
import pandas as pd
import numpy as np
import matplotlib as plt
from matplotlib import pyplot as plt


# In[115]:



path=os.getcwd()
directory = os.path.join(path,"Data")
#print(directory)
#os.chdir(directory)

os.listdir()
nRowsRead = 3600 # specify 'None' if want to read whole file
ALLOWED_EXTENSIONS = set(['csv'])

# The test Image has 2050x800 pixeles 
# Let's change the plot size for use it
plt.rcParams["figure.figsize"] = [20.5, 8] #Inches whit dpi=100 -- 6.4 inches * 100 dpi = 640 pixels
#with lower dpi we get a better resolution, but we need to increase the inches size

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def seedata(df):
    df.head(15)
    
def new_file_name(file):
    file = file.split(".")
    return file[0]

for file in os.listdir():
    if allowed_file(file):
        #print(file)
        df1 = pd.read_csv(file, delimiter=',', nrows = nRowsRead)
        df1["V1"].plot()
        name=new_file_name(file)
        plt.savefig(name+'.png')
        plt.close()
#df1["V1"].plot()
# Dibuja solo N frente a fecha
#df1["MLII"].plot()
# The frecuency (m/s) is : 360 


#plt.rcParams["figure.dpi"]=140


# In[ ]:





# In[ ]:





# In[ ]:




