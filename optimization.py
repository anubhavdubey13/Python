# Optimization

# Min sum(pixi) given bounds for xi, pi's are constants 

import numpy as np
from scipy.optimize import minimize

# def objective1(x,p):
#     tp = x*p
#     return tp

def objective(x):
    return 700*x[0] + 800*x[1]

b1 = (100, 1000)
b2 = (500, 900)
bnds = (b1, b2)

x0 = np.array([900,700])

# res = minimize(objective, x0, method='nelder-mead',
#                options={'xatol': 1e-8, 'disp': True}, bounds=bnds)


def constraint(x):
    return sum(x**2) - 500

con1 = {'type':'ineq', 'fun':constraint}
cons = [con1]

# Incorrect but lemme try
sol = minimize(objective, x0, method = 'SLSQP', bounds = bnds, constraints=cons)

print(sol)