import decimal


decimal.getcontext().prec = 4

pay1 = decimal.Decimal(1)/decimal.Decimal(7)

pay2 = decimal.Decimal(1)/decimal.Decimal(7)

print("pay1:{},pay2:{}".format(pay1,pay2))
