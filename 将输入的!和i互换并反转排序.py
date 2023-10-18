s=[]
n=int(input())
s1=input()
for t in s1:
    s.append(t)
s.reverse()
for i in s:
    if i=='!':
        i='i'
    else:
        i='!'
    print(i,end="")