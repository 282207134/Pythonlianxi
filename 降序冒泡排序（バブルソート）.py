a=int(input())
b=[]
for i in range(a):
    c=int(input())
    b.append(c)
b.sort(reverse=True)
for n in b:
    print(n,end=' ')