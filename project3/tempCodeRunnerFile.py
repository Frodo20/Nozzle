import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from Nozzle.nozzle import nozzle

def main():
    No1 = nozzle(1)
    rho1, v1, T1, Ma1 = No1.cal()
    No1.plot()