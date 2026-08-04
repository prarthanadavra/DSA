def print1(n):
    for i in range(1,n+1):
        for j in range(n):
            print("*", end=" ")
        print()

def print2(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*", end=" ")
        print()

def print3(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()

def print4(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i, end=" ")
        print()

def print5(n):
    for i in range(1,n+1):
        for j in range(1,n-i+2):
            print("*", end=" ")
        print()

def print6(n):
    for i in range(1,n+1):
        for j in range(1,n-i+2):
            print(j, end=" ")
        print()

def print7(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end=" ")
        for k in range(2*i+1):
            print("*", end=" ")
        for l in range(n-i-1):
            print(" ",end=" ")
        print()

def print8(n):
    for i in range(n):
        for j in range(i):
            print(" ",end=" ")
        for k in range(2*n-(2*i+1)):
            print("*", end=" ")
        for l in range(i):
            print(" ",end=" ")
        print()

def print9(n):
    for i in range(1,2*n):
        if i > n:
            i = 2*n-i
        for j in range(i):
            print("*",end=" ")
        print()

def print9(n):
    for i in range(n):
        if i % 2 == 0:
            s = 1
        else:
            s = 0
        for j in range(i+1):
            print(s,end=" ")
            s = 1-s
        print()

print9(5)

