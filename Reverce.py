num = 1234

reverce = 0

while num >0:
    number = num %10
    reverce = reverce * 10 + number
    num = num // 10

print(reverce)