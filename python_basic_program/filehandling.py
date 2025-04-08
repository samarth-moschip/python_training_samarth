#dempstrate file handling 

import shutil 

file1 = open("test.txt", "r")
file2 = open("test2.txt", "w")

for i in range(50):
    line = file1.readline()
    if not line:  
        break
    file2.write(line)

file1.close()
file2.close()

shutil.copy("test2.txt", "/home/samarth/Desktop/test/")

