import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# define the robot parameteres
r = 15 # Radius of the wheels
s = 4 * r # Distance between the wheel centers

# time vector 
timeVector = np.linspace(0, 100, 10000)

# Defive vangular velocity for the wheels
DeltaL = 2*np.ones(timeVector.shape) # left wheel angular velocity
DeltaR = 1.4*np.ones(timeVector.shape) # right wheel angular velocity

# pos  [0] = x, pos[1] = y, pos[2] = theta
def diffModel(pos, t, timePoints, sC, rC, DeltaL_Array, DeltaR_Array):
    # Interpolate the angular velocities for the current time
    DeltaL_t = np.interp(t, timePoints, DeltaL_Array)
    DeltaR_t = np.interp(t, timePoints, DeltaR_Array)
    
    # x_dot
    x_dot = (rC/2*np.cos(pos[2]))*(DeltaR_t + DeltaL_t)
    # y_dot
    y_dot = (rC/2*np.sin(pos[2]))*(DeltaR_t + DeltaL_t)
    # theta_dot
    theta_dot = (rC/sC)*(DeltaR_t - DeltaL_t)

    zeta = [x_dot, y_dot, theta_dot]
    return zeta

# define the initial values for the simulation
# x, y, theta
initialState = np.array([500, 500, 0])

solutionArray = odeint(diffModel, initialState, timeVector, args=(timeVector, s, r, DeltaL, DeltaR))

np.save('simulationData.npy', solutionArray)

# plot the results
plt.plot(timeVector, solutionArray[:, 0], label='x')
plt.plot(timeVector, solutionArray[:, 1], label='y')
plt.plot(timeVector, solutionArray[:, 2], label='theta')
plt.xlabel('time')
plt.ylabel('x, y, theta')
plt.legend()
plt.show()





