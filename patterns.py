def pat(num):
    for i in range(1,num+1):  # 'num' ROWS
        for j in range(1,num-i+1):
            print(end=" ")
        for j in range(i,0,-1):
            print(j,end="")
        for j in range(2,i+1):
            print(j,end="")
        print()

def left_tri(n):
    for i in range(n):
        for j in range(i+1): #change i+1 to n for square pattern
            print("*",end=" ")
        print()

def left_dec_tri(n):
    for i in range(n):
        for j in range(i,n):
            print("*",end=" ")
        print()

def right_tri(n):
    for i in range(n):
        for x in range(i+1,n):
            print(" ",end=" ")
        for y in range(i+1):
            print("*",end=" ")
        print()

def right_dec_tri(n):
    for i in range(n):
        for j in range(i):
            print(" ",end=" ")
        for k in range(i,n):
            print("*",end=" ")
        print()


def hill_pat(n):
    # right_tri(n)
    # left_tri(n)
    for i in range(n):
        #right tri
        for x in range(i,n):
            print(" ",end=" ")
        for y in range(i):
            print("*",end=" ")
        #left Tri
        for z in range(i+1):
            print("*",end=" ")
        print()

def rev_hill_pat(n):
    for i in range(n):
        #right_dec_tri
        for x in range(i+1):
            print(" ",end=" ")
        for y in range(i,n-1):
            print("*",end=" ")
        #left_dec_tri
        for z in range(i,n):
            print("*",end=" ")
        print()

def diamond_pat(n):
    hill_pat(n)
    for i in range(1,n):
        for x in range(i+1):
            print(" ",end=" ")
        for y in range(i,n-1):
            print("*",end=" ")
        for z in range(i,n):
            print("*",end=" ")
        print()

num=5
pat(num)
print("----------------------------------")
left_tri(num)
print("----------------------------------")
left_dec_tri(num)
print("----------------------------------")
right_tri(num)
print("----------------------------------")
right_dec_tri(num)
print("----------------------------------")
hill_pat(num)
print("----------------------------------")
rev_hill_pat(num)
print("----------------------------------")
diamond_pat(num)
