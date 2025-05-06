#two body problem
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FFMpegWriter

'''
assumptions: position = centre of mass of obj, no external forces acting on each body
-- units --
(most of them (should be) in SI units)
1 tick = 1 second
-- credits --
chatgpt: https://chatgpt.com/share/6811a058-7ae0-8005-986b-ddd2a32c8952
video tutroial: https://youtu.be/ToOufaiObV4?si=v2hR2e1AFG1vWU2Z
'''

g_constant = 6.673e-11 #universal grav constant

class Body:
    def __init__(self,mass,position,velocity):
        self.mass = float(mass) #kg
        self.position = np.array(position,dtype=float) #[x,y,z] #m
        self.velocity = np.array(velocity,dtype=float) #[xv,yv,zv] #m/s

    def grav(self,other): #in this func, need ref mass, distance
        arr_diff = other.position - self.position
        distance = np.linalg.norm(arr_diff)
        unit_v = arr_diff/distance

        if distance == 0: return np.zeros(3) #zero check,might change to raise type error 

        force_magnitude = g_constant * ((self.mass*other.mass)/distance**2) #gravity formula
        force_applied = force_magnitude * unit_v
        return force_applied #return 3 val as [xf,yf,zf]
    
    def force_app(self,forces,time): #updates velocity based on forces applied
        #applied forces shld be a 3d list in the direction of forces applied (eg [xf,yf,zf])
        acceleration = forces/self.mass
        self.velocity += acceleration*time     
        pass

    def update(self,time): #update position based on time pass (with velocity)
        self.position += self.velocity*time
        pass

    def kinetic_energy(self):
        v = np.linalg.norm(self.velocity)
        k_e = (1/2)*(self.mass)*(v**2)
        return k_e

class Simulation: 
    def __init__(self,tick = 3600): 
        self.tick = tick #1 tick is 1 second
        self.bodies = [] #list for (both) bodies
        self.time = 0 #also in seconds
        self.position_frame = [] #position of each frame, convert to np.array later

    def edit_tick(self,tick): #for bugfixing/interface implementation
        self.tick = tick

    def add_body(self,mass,position,velocity): #adding a body
        #validation
        if len(position) == 3 and len(velocity) == 3:
            self.bodies.append(Body(mass,position,velocity))          
        #error msg
        else:
            print("Invalid format for position/velocity, must be a list of 3 values")
    
    def time_pass(self,ticks,dpt = 1,saveanim=0): #saveanim is how many ticks each frame is for anim, 0 is no anim/
        if dpt:
            dtick = ticks//dpt
        else: dtick = ticks
        for tick in range(ticks):
            #since theres only 2
            body1 = self.bodies[0]
            body2 = self.bodies[1]

            bg1 = body1.grav(body2)
            bg2 = body2.grav(body1)
            
            body1.force_app(bg1,self.tick)
            body2.force_app(bg2,self.tick)

            body1.update(self.tick)
            body2.update(self.tick)

            self.time += self.tick

            if tick % dtick == 0:
                self.display()

            if saveanim:
                if tick % saveanim == 0:
                    self.position_frame.append([body1.position.copy(),body2.position.copy()])


    def g_potential_energy(self):
        body1 = self.bodies[0]
        body2 = self.bodies[1]
        m_final = body1.mass*body2.mass
        diff = body1.position-body2.position
        dist = np.linalg.norm(diff)
        gpe = -g_constant*((m_final)/dist)
        return gpe

    def total_energy(self):
        return self.g_potential_energy() + sum(body.kinetic_energy() for body in self.bodies)

    def display(self):
        print(f"Time = {self.time} second(s) / {self.time//(3600*24)} day(s) / {round(self.time/(3600*24*365),2)} year(s)")

        for x in range(len(self.bodies)):
            curr_body = self.bodies[x]
            print(f"Body {x+1}")
            print(f"Mass: {curr_body.mass}kg")
            print(f"Position: {curr_body.position} [m]")
            print(f"Velocity: {curr_body.velocity} [m/s]")

        t_energy = self.total_energy()
        print(f"Total energy: {t_energy}J\n")
    
    def create_animation(self):
        if self.position_frame:
            xy1 = np.array(list(x[0][0:2] for x in self.position_frame))
            xy2 = np.array(list(x[1][0:2] for x in self.position_frame)) 
            #basically since self pos frame wld be in [[x,y,z],[x,y,z],...]
            #this grabs the x and y, puts into one list, then converts to np array
            animate_trajectory(xy1,xy2,5.0e7) #manual inp

#original code by arth
def animate_trajectory(position1,position2,limit): #only does x and y for now 
    fig, ax = plt.subplots(figsize=(8, 8)) # creates figure and axis
    # sets limits for x and y axis so that the entire trajectory is shown 
    ax.set_xlim(-limit * 2, limit * 2) 
    ax.set_ylim(-limit * 2, limit * 2)
    ax.set_xlabel("X Position (m)")
    ax.set_ylabel("Y Position (m)")
    ax.set_title("Planetary Motion Simulation")
    ax.grid()
    #ax.scatter(0, 0, color='blue', label="Pluto", s=500)  # adds a grid for better visualisation 
    ax.legend() 
    line1, = ax.plot([], [], lw=2, label="Body 1 Trajectory") # creates the trajectory line
    point1, = ax.plot([], [], 'ro') # creates the red circle for the satellite
    line2, = ax.plot([], [], lw=2,label="Body 2 Trajectory") # creates the trajectory line
    point2, = ax.plot([], [], 'go') # creates the green circle for the satellite

    def update(frame):
        if frame < len(position1):  # Ensure frame index is within bounds
            line1.set_data(position1[:frame, 0], position1[:frame, 1]) # updates trajectory line 
            point1.set_data([position1[frame, 0]], [position1[frame, 1]])  # updates the satellite position 

            line2.set_data(position2[:frame, 0], position2[:frame, 1]) # updates trajectory line 
            point2.set_data([position2[frame, 0]], [position2[frame, 1]])  # updates the satellite position 
        return [line1, point1,line2,point2]

    ani = FuncAnimation(fig, update, frames=len(position1), interval=20, blit=True)
    writer = FFMpegWriter(fps=30)
    ani.save("plt_motion.mp4", writer=writer) # Save as video, ffmpeg to encode
    plt.show()



world = Simulation(tick=3600) 

# pluto (stats from chatgpt)
world.add_body(
    mass=1.29e22,
    position=[-2.37e6, 0.0, 0.0],
    velocity=[0.0, -27.0, 0.0]
)

# charon
world.add_body(
    mass=1.77e21,
    position=[1.73e7, 0.0, 0.0],
    velocity=[0.0, 196.0, 0.0]
)

#simulate
world.time_pass(2000,dpt = 5,saveanim=2) #(amt of ticks to run for, how many displays)

world.display()

world.create_animation()

# Print total energy
print("Total Energy of the System:", world.total_energy())


