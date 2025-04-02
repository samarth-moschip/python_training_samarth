import os
parent_dir="/home/samarth/python"
directory="moschip"
path = os.path.join(parent_dir, directory)
os.mkdir(path)
cwd=os.getcwd()
print(cwd)
