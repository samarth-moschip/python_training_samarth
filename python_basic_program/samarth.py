for i in range(1, 16):  
    for j in range(1, 16):  
        if (i == 1 and j > 1 and j < 15) or (i == 15 and j > 1 and j < 15) or (i == 7 and j > 1 and j < 15) or \
           (j == 1 and i > 1 and i < 7) or (j == 15 and i > 7 and i < 15):
            print("*", end="")
        else:
            print(" ", end="")
    print()
