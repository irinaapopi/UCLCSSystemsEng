import numpy as np
import pandas as pd
from numpy.random import randn
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

rcParams['figure.figsize'] = 5,4
sb.set_style('whitegrid')

x = range(1, 10)
y = [1, 2, 3, 4, 0, 4, 3, 2, 1]

plt.plot(x,y)