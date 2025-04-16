from random import randint, choice

def binary_search(arr, target):
    l, r = 0, len(arr) - 1

    while l <= r:
        m = (l + r) // 2
        
        if arr[m] == target:
            return m
        elif arr[m] > target:
            r = m - 1
        else:
            l = m + 1
    
    return None

grades = set(sorted([randint(75,100) for _ in range(45)]))
grades = list(grades)
target = choice(grades)

log_search = binary_search(grades,target)

if log_search is not None:
    print(f"Item found at index {log_search}")
else:
    print(f"Item {target} cannot be found")
