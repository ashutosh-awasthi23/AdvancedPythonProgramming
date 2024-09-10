import numpy as np
import csv

a = np.arange(1, 17)
s = np.sqrt(a)

np.savetxt('square_root_results_.csv', s, delimiter=' ')


