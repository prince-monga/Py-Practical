cars = ['BMW', 'Audi', 'Toyota', 'Honda']
print("Original list:", cars)
print("First car:", cars[0])
print("Last car:", cars[-1])
print("First two cars:", cars[0:2])

cars.append('Ford')
print("After append:", cars)
cars.insert(2, 'Kia')
print("After insert:", cars)
cars.remove('Audi')
print("After remove:", cars)
popped_car = cars.pop()
print("After pop:", cars)
print("Popped car:", popped_car)

more_cars = ['Hyundai', 'Mercedes']
all_cars = cars + more_cars
print("Concatenated list:", all_cars)

repeated_cars = cars * 2
print("Repeated list:", repeated_cars)

print("Is 'BMW' in cars?", 'BMW' in cars)
print("Is 'Audi' not in cars?", 'Audi' not in cars)

print("Iterating through cars:")
for car in cars:
    print(car)

print("Number of cars:", len(cars))

prices = [40000, 25000, 30000, 22000]
print("Original prices:", prices)
prices.sort()
print("Sorted prices:", prices)
prices.reverse()
print("Reversed prices:", prices)

squared_prices = [p**2 for p in range(1, 5)]
print("Squares using list comprehension:", squared_prices)
