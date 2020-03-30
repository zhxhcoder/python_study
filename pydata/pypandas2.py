import pandas as pd

ret = pd.Series([11.45, 2.67])
print(ret)

print(ret.values)

stock_data = pd.Series([3246.22, 3255.78, 3229.13, 3245.22], index=["open", "high", "low", "close"])
print(stock_data)
print(stock_data["open"])
print(stock_data[["high", "close"]])

sdata = {"open": 3246, "high": 3245, "low": 3299, "close": 3245}
ret = pd.Series(sdata)
print(ret)
