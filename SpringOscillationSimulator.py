Web VPython 3.2
from visual import *
from visual.graph import *
vgraph = gcurve(color=color.green)
xgraph = gcurve(color=color.cyan)
ygraph = gcurve(color=color.blue)
vygraph = gcurve(color=color.yellow)
total = gcurve(color=color.red)
ball = sphere(pos=vector(0,0,0), radius = 10, color=color.cyan)
m_ball = 0.8 # kg
v_ball = vector(0,1,0) # m/s
delta_t = 0.01 # s
t = 0 # s
gravity = vector(0, -9.81 * m_ball, 0)


while t >= 0 and t <= 100 :
    rate(1000)
    spring = vector(0, -(0.5 * ball.pos.y) , 0)
    fnet = gravity + spring
    A = fnet/m_ball
    kinetic = 1/2*m_ball*(mag(v_ball)*mag(v_ball))
    gravitational = m_ball * 9.81 * ball.pos.y
    sprinEnergy = 1/2 * 0.5 * (ball.pos.y * ball.pos.y)
    totalE = kinetic + gravitational + sprinEnergy
    vgraph.plot(pos=(t, kinetic))
    ygraph.plot(pos=(t, gravitational))
    vygraph.plot(pos=(t, sprinEnergy))
    total.plot(pos=(t, totalE))
    v_ball = v_ball + A*delta_t
    ball.pos = ball.pos + (v_ball) * delta_t
    t = t + delta_t
print(t)
    


