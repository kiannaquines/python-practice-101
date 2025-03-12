import random

items = [random.randint(1, 2000) for _ in range(2000)]

n = len(items)


for i in range(n):
    for j in range(n - i - 1):
        if items[j] > items[j + 1]:
            items[j], items[j + 1] = items[j + 1], items[j]

print(f"Bubble sort result: {items}")