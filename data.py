from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class BunNameAndPrice:
    parameters = 'name, price'
    values = [
        ['black bun', 100],
        ['white123', 200],
        ['123', 300]
    ]


class IngredientData:
    parameters = 'name, price, ingredient_type'
    values = [
        [INGREDIENT_TYPE_SAUCE, 100, 'sour cream'],
        [INGREDIENT_TYPE_FILLING, 200, 'cutlet'],
        [INGREDIENT_TYPE_SAUCE, 300, 'cheese']
    ]
