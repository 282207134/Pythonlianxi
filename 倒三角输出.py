a=int(input())
for i in range(a):
    if i==0:
        print("*"*(a-i))
    else:
        print(" "*(i-1),"*"*(a-i))

