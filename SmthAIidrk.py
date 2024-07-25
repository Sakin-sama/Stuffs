import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np


def create_complex_plane(width, height, min_real, max_real, min_imag,
                         max_imag):
  real_values = np.linspace(min_real, max_real, width)
  img_values = np.linspace(min_imag, max_imag, height)
  real, img = np.meshgrid(real_values, img_values)
  complex_plane = real + 1j * img
  return complex_plane


iterations = 50
width = 200
height = 200
min_real = -2
max_real = 2
min_imag = -2
max_imag = 2
grid = create_complex_plane(width, height, min_real, max_real, min_imag,
                            max_imag)
graphing_grid = grid

for i in tqdm(range(height), desc="Processing"):
  for j in range(width):
    z = grid[i, j]
    graphing_grid[i, j] = iterations
    iteration_number = 0
  for number in range(iterations):
    iteration_number = iterations + 1
    z = np.divide((7 * z + 2) - np.cos(np.pi * z) * (5 * z + 2), 4)
    if np.absolute(z) > 10000:
      graphing_grid[i, j] = iterations
      break
    elif np.isnan(z):
      graphing_grid[i, j] = iteration_number
      break
    elif iteration_number == iterations:
      graphing_grid[i, j] = np.absolute(z)
      break
