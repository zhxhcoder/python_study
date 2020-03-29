import decimal
from decimal import Decimal

a = 0.35
b = 0.1

# 0.44999999999999996 默认15位精度
print(a + b)

# 默认28位精度
print(decimal.getcontext())
print(Decimal(0.35) + Decimal(0.1))

decimal.getcontext().prec = 3
print(Decimal(0.35) + Decimal(0.1))

decimal.getcontext().prec = 4
print(Decimal(0.35) + Decimal(0.1))

decimal.getcontext().prec = 66
print(Decimal(0.35) + Decimal(0.1))
