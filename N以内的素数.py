N=int(input())
i = 2
while(i < N):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print(i)
   i = i + 1
