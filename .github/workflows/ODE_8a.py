from numpy import *
from matplotlib.pyplot import *

w=1

def f(r,t):
	x=r[0]
	xdot=r[1]
	fx=xdot
	fxdot=-w**2*x
	return array([fx,fxdot],float)

t_initial=0.0
t_final=50.0
N=1000
h=(t_final-t_initial)/N
x_0=1
xdot_0=0
tpoints=arange(t_initial,t_final+h,h)
xpoints=[]
r=array([x_0,xdot_0],float)

for t in tpoints:
	xpoints.append(r[0])
	k1=h*f(r,t)
	k2=h*f(r+0.5*k1,t+0.5*h)
	k3=h*f(r+0.5*k2,t+0.5*h)
	k4=h*f(r+k3,t+h)
	r+=(k1+2*k2+2*k3+k4)/6.0
plot(tpoints,xpoints)
xlabel('time')
ylabel('x')
savefig('harmonic.pdf')
show()
