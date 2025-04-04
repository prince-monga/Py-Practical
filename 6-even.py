count = 0
num = 0

while True:
    if num % 2 != 0:
        num += 1
        continue  

    print(num)
    count += 1
    if count == 5:
        break  

    num += 1
