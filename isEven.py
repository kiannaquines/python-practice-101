def isEven(n):
    if n == 0:
        return True

    if n % 2 == 0:
        return True
    
    return False

import random

numbers = [random.randint(0, 100) for _ in range(100)]

for number in numbers:

    isEvenResult = isEven(number)
    print(f'{number} {isEvenResult}')
