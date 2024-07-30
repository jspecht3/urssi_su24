import numpy as np
from scipy.optimoze import minimize

from rosen.example import rosen, rosen_der

x0 = np.array([1.3,0.7,0.8,1.9,1.2])
result = minimize(rosen, x0, method="BFGS", jac=rosen_der, optins={"disp": True})
optimized_params = result.x
