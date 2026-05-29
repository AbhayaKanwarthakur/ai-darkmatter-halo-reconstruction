import numpy as np

def isothermal_density(r, rho0, rc):
    return rho0 / (1 + (r/rc)**2)

def burkert_density(r, rho0, rb):
    return rho0 / ((1 + r/rb) * (1 + (r/rb)**2))

def einasto_density(r, rho_e, re, alpha):
    return rho_e * np.exp(-(r/re)**alpha)

def nfw_density(r, rho_s, rs):
    return rho_s / ((r/rs) * (1 + r/rs)**2)
