# for minimum reqtangle integral any random points 

import numpy as np 

def montecarlo_rectangular(area,totaldot)
  inside = 0
  
  for i in range(0, tot):
    # Generate random x, y in [0, 1].
    x = np.random.rand()
    y = np.random.rand()
      # Increment if inside unit circle.
    if (x*y) <area:     
        inside += 1

  square = float(inside) / total

  # It works!
  return square
