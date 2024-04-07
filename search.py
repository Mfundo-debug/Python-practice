"""
Make use of maxwell's equations to find the electric field of a point charge.
use the following constants:
k = 8.99e9
q = 1e-9
r = 1

"""
import math
import numpy as np

def electric_field(q, r):
    k = 8.99e9
    E = k*q/r**2
    return E

if __name__ == '__main__':
    q = 1e-9
    r = 1
    E = electric_field(q, r)
    print(f'The electric field of a point charge is {E}')