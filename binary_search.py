import random

def binary_search(items, target):
    left, right = 0, len(items) - 1

    while left <= right:
        middle = (left + right) // 2
        if items[middle] == target:
            return middle
        elif items[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    
    return -1

if __name__ == "__main__":
    grades = list(set(sorted([random.randint(75,100) for _ in range(50)])))
    target = random.choice(grades)
    print(grades)
    print(target)
    search = binary_search(grades, target)
    print(search)
