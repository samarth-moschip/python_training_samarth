import os

print(os.getcwd())

path = os.getcwd()
print(os.listdir(path))

list1 = os.listdir()
for i in range(len(list1)):
    base, ext = os.path.splitext(list1[i])
    os.rename(list1[i], base + ".py")
