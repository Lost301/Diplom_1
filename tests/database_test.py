import pytest

from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def database():
    return Database()


class TestDatabase:

    def test_available_buns_count_is_three(self, database):
        buns = database.available_buns()

        assert len(buns) == 3

    def test_available_buns_names(self, database):
        buns = database.available_buns()

        assert [bun.get_name() for bun in buns] == ['black bun', 'white bun', 'red bun']

    def test_available_buns_prices(self, database):
        buns = database.available_buns()

        assert [bun.get_price() for bun in buns] == [100, 200, 300]

    def test_available_ingredients_count_is_six(self, database):
        ingredients = database.available_ingredients()

        assert len(ingredients) == 6

    def test_available_ingredients_names(self, database):
        ingredients = database.available_ingredients()

        assert [i.get_name() for i in ingredients] == [
            'hot sauce', 'sour cream', 'chili sauce',
            'cutlet', 'dinosaur', 'sausage',
        ]

    def test_available_ingredients_prices(self, database):
        ingredients = database.available_ingredients()

        assert [i.get_price() for i in ingredients] == [100, 200, 300, 100, 200, 300]

    def test_available_ingredients_types(self, database):
        ingredients = database.available_ingredients()

        assert [i.get_type() for i in ingredients] == [
            INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE,
            INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING,
        ]
