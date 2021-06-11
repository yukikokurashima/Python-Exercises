print("Second Number Pattern")

lastNumber = 6

for row in range(1, lastNumber):
    for column in range(1, row + 1):
        print(row, end=' ')
    print("")

print()

for i in range(1, 5 + 1):
    for j in range(1, 5 + 1):
        print(i, end=' ')
    print()

print()

for i in range(1, 5 + 1):
    print(i)

print()

for i in range(1, 5 + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
