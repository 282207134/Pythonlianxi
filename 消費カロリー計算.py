exercise=input()
time=float(input())
weight=float(input())
METs=0
if exercise=='push-ups':
    METs=8.0
elif exercise=='sit-ups':
    METs=8.0
elif exercise=='squats':
    METs=5.0
elif exercise=='walking':
    METs=3.3
else:
    METs=4.0
calorie=int(time*weight*METs*1.05)
print(calorie)