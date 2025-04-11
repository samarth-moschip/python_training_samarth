#program to print some pattern in python

for i in range(1, 16):  
    for j in range(1, 16):  
        if (i==1) or (j==1 and i<=7) or (i==7) or (j==15 and i>7 and i<=15) or i==15 or ( i>=7 and j<=i and  i+j<=15)or (i>=j and i<7 and j<7) or j==1 or j==15 :    
            print("*", end="")
        else:
            print(" ", end="")
    print() 
