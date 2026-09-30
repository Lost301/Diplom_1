import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize('ingredient_type, name, price', [
        (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
        (INGREDIENT_TYPE_FILLING, 'cutlet', 100),
        (INGREDIENT_TYPE_SAUCE, '', 0),
    ])
    def test_get_type_returns_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize('name', ['hot sauce', 'sour cream', 'cutlet', ''])
    def test_get_name_returns_name(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 100)

        assert ingredient.get_name() == name

    @pytest.mark.parametrize('price', [0, 100, 300.5])
    def test_get_price_returns_price(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'sausage', price)

        assert ingredient.get_price() == price
