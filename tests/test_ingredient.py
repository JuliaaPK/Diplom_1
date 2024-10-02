import pytest

import data
from praktikum.ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize(data.IngredientData.parameters, data.IngredientData.values)
    def test_get_ingredient_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize(data.IngredientData.parameters, data.IngredientData.values)
    def test_get_ingredient_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize(data.IngredientData.parameters, data.IngredientData.values)
    def test_get_ingredient_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
