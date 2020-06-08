import matplotlib.pyplot as plt
import statsmodels.api as sm

data = sm.datasets.ccard.load_pandas().data
plt.scatter(data['INCOMESQ'], data['INCOME'])
