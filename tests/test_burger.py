from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestBurger:
    # Используем мокирование булки
    def test_set_bun(self):
        bun_mock = Mock()
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun is not None

    # Используем мокирование ингредиента
    def test_add_ingredient(self):
        ingredient_mock = Mock()
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self):
        ingredient_mock = Mock()
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        first_ingredient = Mock()
        burger = Burger()
        burger.add_ingredient(first_ingredient)
        second_ingredient = Mock()
        burger.add_ingredient(second_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == second_ingredient and burger.ingredients[1] == first_ingredient

    def test_get_price(self):
        bun = Bun('chili', 100)
        burger = Burger()
        burger.set_buns(bun)
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'cheese', 300)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == 500
