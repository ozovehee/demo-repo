from forex_python.converter import CurrencyRates
cur = CurrencyRates()
amount = int(input("Enter the amount: "))
from_curr = input("From Currency: ").upper()
to_curr = input("To Currency: ").upper()

print(from_curr, " to ", to_curr, amount)
result = cur.convert(from_curr, to_curr, amount)
print(result)