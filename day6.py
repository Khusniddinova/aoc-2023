'''

import math
time=[int(x) for x in input().split(' ')]
dist=[int(a) for a in input().split(' ')]
cnt=1

for i in range(len(time)):
    w=0
    d=time[i]**2-4*dist[i]
    x=math.ceil((time[i]-d**(1/2))/2)
    if ((x*(time[i]-x))<=dist[i]):
        x=x+1
    w=time[i]-x-x+1
    cnt=cnt*w

print(cnt)
'''
import math
time=[str(x) for x in input().split(' ')]
dist=[str(a) for a in input().split(' ')]
t="".join(time)
d="".join(dist)
t1=int(t)
d1=int(d)
x=math.ceil((t1-(t1**2-4*d1)**(1/2))/2)
print(t1-x-x+1)

