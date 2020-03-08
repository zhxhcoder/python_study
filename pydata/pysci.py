import numpy as np
from scipy import stats

np.random.seed(12345678)
x = stats.norm.rvs(loc=0, scale=1, size=300)
print(stats.kstest(x, 'norm'))
