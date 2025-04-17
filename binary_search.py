from random import randint, choice

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    
    return -1

if __name__ == "__main__":
    grades = [randint(75,100) for _ in range(50)]
    grades = sorted(list(set(grades)))
    search = binary_search(grades, choice(grades))

    if search > -1:
        print(f"Item found in {search}")
    else:
        print(f"Item cannot be found")
