numbers = [1,2,3,3,4,4,5,6,6,6]

Duplicate = []

for num in numbers:
    if numbers.count(num) > 1 and num not in Duplicate:
        Duplicate.append(num)

print(Duplicate)