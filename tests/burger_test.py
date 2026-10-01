from unittest.mock import Mock

import pytest

from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun():
    bun = Mock()
    bun.get_name.return_value = 'black bun'
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def sauce():
    ingredient = Mock()
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ingredient.get_name.return_value = 'hot sauce'
    ingredient.get_price.return_value = 100
    return ingredient


@pytest.fixture
def filling():
    ingredient = Mock()
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    ingredient.get_name.return_value = 'cutlet'
    ingredient.get_price.return_value = 200
    return ingredient


class TestBurger:

    def test_set_buns_sets_bun(self, burger, bun):
        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient_adds_to_list(self, burger, sauce, filling):
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        assert burger.ingredients == [sauce, filling]

    def test_remove_ingredient_removes_by_index(self, burger, sauce, filling):
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        burger.remove_ingredient(0)

        assert burger.ingredients == [filling]

    def test_move_ingredient_changes_position(self, burger, sauce, filling):
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        burger.move_ingredient(1, 0)

        assert burger.ingredients == [filling, sauce]

    @pytest.mark.parametrize('bun_price, ingredient_prices, expected', [
        (100, [], 200),
        (100, [100], 300),
        (100, [100, 200], 500),
        (0, [0], 0),
    ])
    def test_get_price_sums_prices(self, burger, bun_price, ingredient_prices, expected):
        burger.bun = Mock()
        burger.bun.get_price.return_value = bun_price
        for price in ingredient_prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            burger.add_ingredient(ingredient)

        assert burger.get_price() == expected

    def test_get_receipt_contains_bun_ingredients_and_price(self, burger, bun, sauce, filling):
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        receipt = burger.get_receipt()

        assert receipt == (
            '(==== black bun ====)\n'
            '= sauce hot sauce =\n'
            '= filling cutlet =\n'
            '(==== black bun ====)\n'
            '\n'
            'Price: 500'
        )
