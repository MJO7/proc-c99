# code to delete all the files in a folder older than 30 days.
import shutil
import time
import os
seconds = time.time()
# dir = '/Users/rachanajoshi/Desktop/C-99'
dir = input("Enter name of the directory you want to clean:")
ctime = os.stat(dir).st_ctime
for f in os.listdir(dir):
    if(seconds-ctime>=2592000):
        os.remove(os.path.join(dir, f))
        print("Directory is cleaned.")
    else :
        print("No file found older than 30 days.")