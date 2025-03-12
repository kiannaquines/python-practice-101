import random

items = [random.randint(1, 3000) for _ in range(3000 + 1)]
n = len(items)


for i in range(n):
    for j in range(n - i - 1):
        if items[j] > items[j + 1]:
            items[j + 1], items[j] = items[j], items[j + 1]

print(f"Bubble Sort: {items}")