Web VPython 3.2
    
# Parameters
r = 5 
t = 0.2 
s = 50
N = 1 # number of loops
I = 1 # current
Mu0 = 12.57e-7
obs = [] # creates list used to store observation locations
Q = 1.6e-19
Mass = 1.67e-27

dtheta = pi/6
theta = 0

sf = 0.15e8
# Create the ring
rin = ring(pos=vec(0, 0, 0), axis=vec(0, 1, 0), radius = r, thickness = t, color=color.white)

dtheta = pi/6
theta = 0
obsy = 0

while theta < 2*pi:
    a = arrow(pos=vec(r * cos(theta), obsy, r * sin(theta)), axis=vector(0,0,0), color=color.green)
    obs.append(a)
    theta = theta + dtheta
    
    
j = 0 

while j < len(obs):
    rate(500)
    barrel = obs[j]
    B_net = vector(0,0,0)
    r = obs[j].pos - rin.pos
    rhat = r/r.mag
    B = (Mu0 * N * I)/(2*pi*r.mag) 
    rperp = rotate(r, angle = pi/2, axis=vector(0,1,0))
    B_net = B * rperp
    barrel.axis = B_net * sf

    print(r)
    print(rperp)

    j = j + 1
    
t = 0
deltat = 1e-10
proton = sphere(pos=vec(6,0,0), radius = 0.3, color=color.red, make_trail=True)
r = proton.pos - rin.pos
v_proton = vector(-5e4,0,0)


while t < 20:
    rate(1000000)
    r = proton.pos - rin.pos
    B = (Mu0 * N * I)/(2*pi*r.mag) * 10000
    rperp = rotate(r, angle = pi/2, axis=vector(0,1,0))
    B_net = B * rperp
    B_force = Q * (v_proton.cross(B_net))
    #print(B_force)
    a = B_force / Mass
    v_proton = v_proton + (a * deltat)
    #print(v_proton)
    proton.pos = proton.pos + (v_proton * deltat)
    t = t + deltat
    

