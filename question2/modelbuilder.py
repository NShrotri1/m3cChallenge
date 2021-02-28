import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility

x = [1,2,3,4]
y = [17,25,21,37]
colors = np.random.rand(len(x))
area = 15

plt.scatter(x, y, s=area, c=colors, alpha=1)
plt.show()
