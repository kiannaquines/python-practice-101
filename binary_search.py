import random

numbers = [random.randint(0, 100) for _ in range(100)]
numbers = sorted(numbers)


def binary_search(numbers,target):
  left, right = 0, len(numbers) - 1

  while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == target:
      return mid
    elif numbers[mid] > target:
      right = mid + 1
    else:
      left = mid + 1

  return -1


search = binary_search(numbers,89)

if search is not None:
  print(f"Item found at index {search}")
else:
  print("Item cannot be found")
