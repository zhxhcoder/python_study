import statsmodels.api as sm
import matplotlib.pyplot as plt
data = sm.datasets.ccard.load_pandas().data
plt.scatter(data['INCOMESQ'], data['INCOME'])