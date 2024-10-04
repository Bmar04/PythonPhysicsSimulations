Web VPython 3.2
from __future__ import division, print_function
from visual import *
scene.width = scene.height = 800
## constants
oofpez = 0.22 # stands for One Over Four Pi Epsilon-Zero
qe = 1.6e-19
s = 4e-11
t = 0 #Seconds
deltat = 1e-6
mproton = 1.6e-27
scalefactor = 1.0e-9 # you may need to change this
p1 = sphere(pos=vector(0,s/2,0), radius=1e-11, color=color.red)
q1 = qe
p2 = sphere(pos=vector(0,-s/2,0), radius=1e-11, color=color.blue)
q2 = -qe
proton = sphere(pos=vector(-3*s,0,0), radius = 1e-11, color=color.green, make_trail=True)
vproton = vector(0,0,0)

#proton loop
while t>= 0 and t<=1.43e-3:
    rate(300)
    rpos = vector(0,s/2,0) - proton.pos
    dpos = mag(rpos)
    rhatpos = rpos / dpos
    eFieldpos = (((oofpez) * ((q1 * s))) / pow((dpos), 2)) * rhatpos
    rneg = vector(0,-s/2,0) - proton.pos
    dneg = mag(rneg)
    rhatneg = rneg / dneg
    eFieldneg = (((oofpez) * ((q2 * s))) / pow((dneg), 2)) * rhatneg
    
    eField = eFieldpos + eFieldneg
    
    
    fnet = eField * qe
    A = fnet/mproton
    vproton = vproton + (A * deltat)
    proton.pos = proton.pos + (vproton * deltat)
    t = t + deltat
    print (eField)
    
    
proton.pos = vector(-3*s,0,0)

while t>= 0 and t<=2.15e-3:
    rate(300)
    rpos = vector(0,s/2,0) - proton.pos
    dpos = mag(rpos)
    rhatpos = rpos / dpos
    eFieldpos = (((oofpez) * ((q1 * s))) / pow((dpos), 2)) * rhatpos
    rneg = vector(0,-s/2,0) - proton.pos
    dneg = mag(rneg)
    rhatneg = rneg / dneg
    eFieldneg = (((oofpez) * ((q2 * s))) / pow((dneg), 2)) * rhatneg
    
    eField = eFieldpos + eFieldneg
    
    
    fnet = eField * -qe
    A = fnet/mproton
    vproton = vproton + (A * deltat)
    proton.pos = proton.pos + (vproton * deltat)
    t = t + deltat
    print (eField)
    
proton.make_trail = False
proton.pos = vector(-3*s, -2*s,0)
proton.make_trail = True


while t>= 0 and t<=3e-3:
    rate(300)
    rpos = vector(0,s/2,0) - proton.pos
    dpos = mag(rpos)
    rhatpos = rpos / dpos
    eFieldpos = (((oofpez) * ((q1 * s))) / pow((dpos), 2)) * rhatpos
    rneg = vector(0,-s/2,0) - proton.pos
    dneg = mag(rneg)
    rhatneg = rneg / dneg
    eFieldneg = (((oofpez) * ((q2 * s))) / pow((dneg), 2)) * rhatneg
    
    eField = eFieldpos + eFieldneg
    
    
    fnet = -1 * (eField * qe)
    A = fnet/mproton
    vproton = vproton + (A * deltat)
    proton.pos = proton.pos + (vproton * deltat)
    t = t + deltat
    print (eField)
    
