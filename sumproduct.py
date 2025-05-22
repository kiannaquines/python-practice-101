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

ingredient_info = [
    {
        'item': 'Corn',
        'weight': 1,
        'price': 75,
        'category': 'Energy',
        'composition': {
            'cp': 7.80,
            'cfat': 3.40,
            'cfiber': 2.80,
            'me': 3.30,
            'calcium': 0.07,
            'totalP': 0.25,
            'availP': 0.06,
            'lysine': 0.26,
            'met': 0.18,
            'm+c': 0.36,
        },
        'constraints': {
            'min': 45,
            'max': 100,
        }
    },
    {
        'item': 'Soybean Meal',
        'weight': 1,
        'price': 100,
        'category': 'Protein',
        'composition': {
            'cp': 43.10,
            'cfat': 1.80,
            'cfiber': 5.00,
            'me': 2.24,
            'calcium': 0.45,
            'totalP': 0.63,
            'availP': 0.19,
            'lysine': 2.73,
            'met': 0.63,
            'm+c': 1.29,
        },
        'constraints': {
            'min': 0,
            'max': 100,
        }
    },
    {
        'item': 'Skimmilk',
        'weight': 1,
        'price': 250,
        'category': 'Protein',
        'composition': {
            'cp': 33.50,
            'cfat': 0.50,
            'cfiber': 0,
            'me': 2.51,
            'calcium': 1.25,
            'totalP': 0.95,
            'availP': 0.95,
            'lysine': 2.68,
            'met': 0.54,
            'm+c': 1.27,
        },
        'constraints': {
            'min': 2,
            'max': 100,
        }
    },
    {
        'item': 'Rice bran D1',
        'weight': 1,
        'price': 80,
        'category': 'Energy',
        'composition': {
            'cp': 12.40,
            'cfat': 13.30,
            'cfiber': 4.40,
            'me': 2.40,
            'calcium': 0.07,
            'totalP': 1.51,
            'availP': 0.23,
            'lysine': 0.57,
            'met': 0.26,
            'm+c': 0.52,
        },
        'constraints': {
            'min': 5,
            'max': 100,
        }
    },
    {
        'item': 'Fish Meal',
        'weight': 1,
        'price': 150,
        'category': 'Protein',
        'composition': {
            'cp': 58.70,
            'cfat': 12.50,
            'cfiber': 0.50,
            'me': 2.80,
            'calcium': 4.68,
            'totalP': 2.86,
            'availP': 2.86,
            'lysine': 4.22,
            'met': 1.56,
            'm+c': 2.11,
        },
       'constraints': {
            'min': 1,
            'max': 50,
      }
    },
     {
        'item': 'Coconut Oil',
        'weight': 1,
        'price': 50,
        'category': 'Energy',
        'composition': {
            'cp': 0,
            'cfat': 99,
            'cfiber': 0,
            'me': 8.60,
            'calcium': 0,
            'totalP': 0,
            'availP': 0,
            'lysine': 0,
            'met': 0,
            'm+c': 0,
        },
       'constraints':{
            'min': 0,
            'max': 100,
       }
    },
    {
        'item': 'Limestone',
        'weight': 1,
        'price': 6.30,
        'category': 'Additive',
        'composition': {
            'cp': 0,
            'cfat': 0,
            'cfiber': 0,
            'me': 0,
            'calcium': 38,
            'totalP': 0.16,
            'availP': 0,
            'lysine': 0,
            'met': 0,
            'm+c': 0,
        },
        'constraints': {
            'min': 0,
            'max': 100,
        }
    },
    {
        'item': 'Monodical Phosphate',
        'weight': 1,
        'price': 80,
        'category': 'Additive',
        'composition': {
            'cp': 0,
            'cfat': 0,
            'cfiber': 0,
            'me': 0,
            'calcium': 16,
            'totalP': 21,
            'availP': 18,
            'lysine': 0,
            'met': 0,
            'm+c': 0,
        },
        'constraints': {
            'min': 0,
            'max': 100,
        }
    },
     {
        'item': 'Vitamin Premix',
        'weight': 1,
        'price': 185,
        'category': 'Additive',
        'composition': {
            'cp': 0,
            'cfat': 0,
            'cfiber': 0,
            'me': 0,
            'calcium': 0,
            'totalP': 0,
            'availP': 0,
            'lysine': 0,
            'met': 0,
            'm+c': 0,
        },
        'constraints': {
            'min': 0.25,
            'max': 0.25,
        }
    },
    {
        'item': 'Choline',
        'weight': 1,
        'price': 640,
        'category': 'Additive',
        'composition': {
            'cp': 0,
            'cfat': 0,
            'cfiber': 0,
            'me': 0,
            'calcium': 0,
            'totalP': 0,
            'availP': 0,
            'lysine': 0,
            'met': 0,
            'm+c': 0,
        },
       'constraints': {
            'min': 0.25,
            'max': 0.25,
       }
    },
    {
        'item': 'Salt',
        'weight': 1,
        'price': 28,
        'category': 'Additive',
        'composition': {
            'cp': 0,
            'cfat': 0,
            'cfiber': 0,
            'me': 0,
            'calcium': 0,
            'totalP': 0,
            'availP': 0,
            'lysine': 0,
            'met': 0,
            'm+c': 0,
        },
        'constraints': {
            'min': 0.25,
            'max': 0.25,
        }
    },
    {
        'item': 'L-lysine',
        'weight': 1,
        'price': 1279,
        'category': 'Additive',
        'composition': {
            'cp': 74,
            'cfat': 0,
            'cfiber': 0,
            'me': 3.63,
            'calcium': 0,
            'totalP': 0,
            'availP': 0,
            'lysine': 78.80,
            'met': 0,
            'm+c': 0,
        },
        'constraints': {
            'min': 0.25,
        'max': 0.25,
        }
    },
    {
        'item': 'DL-Methionine',
        'weight': 1,
        'price': 120,
        'category': 'Additive',
        'composition': {
            'cp': 58,
            'cfat': 0,
            'cfiber': 0,
            'me': 3.60,
            'calcium': 0,
            'totalP': 0,
            'availP': 0,
            'lysine': 0,
            'met': 99,
            'm+c': 0,
        },
        'constraints': {
            'min': 0,
        'max': 100,
        }
    },
    {
        'item': 'Antioxidant-Santo/Ethox',
        'weight': 1,
        'price': 200,
        'category': 'Additive',
        'composition': {
            'cp': 0,
            'cfat': 0,
            'cfiber': 0,
            'me': 0,
            'calcium': 0,
            'totalP': 0,
            'availP': 0,
            'lysine': 0,
            'met': 0,
            'm+c': 0,
        },
        'constraints': {
            'min': 0.25,
            'max': 0.25,
        }
    },
    {
        'item': 'Azolla',
        'weight': 1,
        'price': 350,
        'category': 'Energy',
        'composition': {
            'cp': 21.30,
            'cfat': 0,
            'cfiber': 15.30,
            'me': 1.0513,
            'calcium': 0.45,
            'totalP': 0,
            'availP': 0.35,
            'lysine': 0,
            'met': 1.40,
            'm+c': 0,
        },
       'constraints': {
            'min': 5,
            'max': 5,
       }
    }
]
