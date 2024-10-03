import pytest

from data import IngredientData
from praktikum.ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize("price", IngredientData.values_for_price)
    def test_get_ingredient_price(self, price):
        ingredient = Ingredient(IngredientData.static_ingredient_type, IngredientData.static_name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize("name", IngredientData.values_for_name)
    def test_get_ingredient_name(self, name):
        ingredient = Ingredient(IngredientData.static_ingredient_type, name, IngredientData.static_price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type", IngredientData.values_for_ingredient_type)
    def test_get_ingredient_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, IngredientData.static_name, IngredientData.static_price)
        assert ingredient.get_type() == ingredient_type
