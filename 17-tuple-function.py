cars = ('BMW', 'Audi', 'Toyota', 'Honda', 'Audi')

print("Original tuple:", cars)
print("First car:", cars[0])
print("Last car:", cars[-1])
print("First three cars:", cars[:3])

print("Length of tuple:", len(cars))
print("Count of 'Audi':", cars.count('Audi'))
print("Index of 'Toyota':", cars.index('Toyota'))

print("Is 'Honda' in cars?", 'Honda' in cars)
print("Is 'Ford' not in cars?", 'Ford' not in cars)

for car in cars:
    print(car)

numbers = (4, 1, 3, 2)
sorted_numbers = tuple(sorted(numbers))
print("Sorted tuple:", sorted_numbers)
reversed_numbers = tuple(reversed(numbers))
print("Reversed tuple:", reversed_numbers)
