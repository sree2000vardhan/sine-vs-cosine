import numpy as np
from matplotlib import pyplot as plt
from math import sin,cos
import math
p=[]
q=[]
r=[]
print("select the desired sine vs. cosine curves")
k=int(input("1.In Radians 2.In degress\n"))
if k==1:
    print("please input how many sine and cosine values you want to plot")
    z=int(input())
    for i in range(z):
        x=float(input("enter values for sine and cosine in Radians\n"))
        p.append(x)
    p=sorted(p)
    for i in p:
        y1=sin(i)
        q.append(y1)
        y2=cos(i)
        r.append(y2)
        
    plt.figure(figsize=(10,10))
    plt.yticks(np.arange(-1,1.1,0.05))
    plt.plot(p,q,color='g',linewidth=1,alpha=1,marker="o",label="Sine curve")
    plt.plot(p,r,color='y',linewidth=1,alpha=1,marker="*",label="Cosine curve")
    plt.title("Sine Vs. Cosine Curve in Radians",color="r")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True,color='b')
    plt.show()
elif k==2:
    print("please input how many sine and cosine values you want to plot")
    z=int(input())
    for i in range(z):
        x=float(input("enter values for sine and cosine in degrees\n"))
        p.append(x)
    p=sorted(p)
    for j in p:
        w=j*(math.pi/180)
        y1=sin(w)
        q.append(y1)
        y2=cos(w)
        r.append(y2)
    plt.figure(figsize=(10,10))
    plt.yticks(np.arange(-1,1.1,0.05))
    plt.plot(p,q,color='g',linewidth=1,alpha=1,marker='o',label="Sine curve")
    plt.plot(p,r,color='y',linewidth=1,alpha=1,marker='*',label="Cosine curve")
    plt.title("Sine Vs. Cosine Curve in Degrees",color="r")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True,color='b')
    plt.show()
    
else:
    print("Invalid input")
    
    





