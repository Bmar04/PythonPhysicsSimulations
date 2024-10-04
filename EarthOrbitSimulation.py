Web VPython 3.2
from visual import *

G = 6.7e-11
rearth = 6.4e6
rmoon = 9e6
mearth = 6e24 #kg
mrocket = 173 #kg
mmoon = 7.3e22 #kg

#rearth*60 = distance from earth to moon


earth = sphere(pos=vec(0,0,0), radius = rearth, color=color.cyan)
moon = sphere(pos=earth.pos+ vec(rearth*60,0,0), radius = rmoon, color=color.white, make_trail=True)
moon.v = vec(0,1022,0)
moon.p = mmoon*moon.v
fgmoon = vec(0,0,0)

rocket = sphere(pos=earth.pos + vec(-1*rearth+50,0,0), radius = 500, color=color.red, make_trail=True)
rocket.v = vec(-4910,9996,0)
rocket.p = mrocket*rocket.v
fgrocket = vec(0,0,0)

deltat=10
t=0 #Seconds

scene.center = vec(100*rearth,0,0)

#Animation Loop
while t<350000: 
    rate(10000)
    #Calculate the distance between objects
    vec.r2 = (rocket.pos-earth.pos)
    vec.r3 = (rocket.pos-moon.pos)
    vec.r2mag=mag(vec.r2)
    vec.r3mag=mag(vec.r3)
    
    #Calculates the net force of the rocket from the moon and earth
    fgrocket = (-G*((mearth*mrocket)/(vec.r2mag**2))*(vec.r2/vec.r2mag))+(-G*((mmoon*mrocket)/(vec.r3mag**2))*vec.r3/vec.r3mag)

    vec.r1 = moon.pos-earth.pos
    vec.r1mag=mag(vec.r1)
    fgmoon = -G*((mearth*mmoon)/(vec.r1mag**2))*(vec.r1/vec.r1mag) + vec(5000,5000,5000)
    
    moon.p = moon.p+fgmoon*deltat
    moon.v = moon.p/mmoon
    moon.pos = moon.pos + moon.v*deltat
    
    rocket.p = rocket.p + fgrocket*deltat
    rocket.v = rocket.p/mrocket
    rocket.pos= rocket.pos+rocket.v*deltat
    
    t=t+deltat
    
print(rocket.v)
