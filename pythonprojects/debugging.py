prices = [5, 10, 15, 20, 10]

total = 0

for price in prices:
    total += price

if total >= 50:
    discount = total * 0.10
    total = total - discount

print("Total:", total)