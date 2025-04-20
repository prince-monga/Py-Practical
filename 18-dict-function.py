car_prices = {'BMW': 50000, 'Audi': 45000, 'Toyota': 30000, 'Honda': 28000}

print("Original dictionary:", car_prices)
print("Price of BMW:", car_prices['BMW'])

car_prices['Ford'] = 25000
print("After adding Ford:", car_prices)

car_prices['Audi'] = 46000
print("After updating Audi price:", car_prices)

del car_prices['Toyota']
print("After deleting Toyota:", car_prices)

print("All keys:", list(car_prices.keys()))
print("All values:", list(car_prices.values()))
print("All items:", list(car_prices.items()))

print("Is 'Honda' in dictionary?", 'Honda' in car_prices)
print("Is 'Toyota' not in dictionary?", 'Toyota' not in car_prices)

for car, price in car_prices.items():
    print(car, "->", price)

price_copy = car_prices.copy()
print("Copied dictionary:", price_copy)

car_prices.clear()
print("After clearing:", car_prices)
