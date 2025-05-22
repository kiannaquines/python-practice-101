def sumproduct(a, b, percent=False):
    total = sum(x * y for x, y in zip(a, b))
    return total / 100 if percent else total

for nutrient in nutrients:
    if nutrient in ['weight', 'price']:
        nutrient_values = [ingredient[nutrient] for ingredient in ingredient_info]
    else:
        nutrient_values = [ingredient['composition'][nutrient] for ingredient in ingredient_info]

    result = sumproduct(nutrient_values, ingredient_inclusion, percent=True)
    diet_composition.append(result)
    print(f"{nutrient}: {result:.4f}")
