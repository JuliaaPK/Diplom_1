from unittest.mock import Mock

from praktikum.database import Database


class TestDataBase:
    def test_database_available_buns(self):
        database = Database()
        first_bun = Mock()
        second_bun = Mock()
        database.buns = []
        database.buns.append(first_bun)
        database.buns.append(second_bun)
        available_buns = database.available_buns()
        assert first_bun in available_buns and second_bun in available_buns

    def test_database_available_ingredients(self):
        database = Database()
        first_ingredient = Mock()
        second_ingredient = Mock()
        database.ingredients = []
        database.ingredients.append(first_ingredient)
        database.ingredients.append(second_ingredient)
        available_ingredients = database.available_ingredients()
        assert first_ingredient in available_ingredients and second_ingredient in available_ingredients
