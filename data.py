from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class BunParameters:
    values_for_name = [
        ['black bun'],
        ['white123'],
        ['123']
    ]

    values_for_price = [
        ['black bun'],
        ['white123'],
        ['123']
    ]

    static_name = 'bun'
    static_price = 200


class IngredientData:
    values_for_name = [
        ['sour cream'],
        ['cutlet'],
        ['cheese']
    ]

    values_for_price = [
        [100],
        [200],
        [300]
    ]

    values_for_ingredient_type = [
        [INGREDIENT_TYPE_SAUCE],
        [INGREDIENT_TYPE_FILLING],
        [INGREDIENT_TYPE_SAUCE]
    ]

    static_name = 'cheese'
    static_price = 200
    static_ingredient_type = INGREDIENT_TYPE_SAUCE
