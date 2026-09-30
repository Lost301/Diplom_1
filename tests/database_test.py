from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_available_buns_returns_three_buns(self):
        database = Database()
        buns = database.available_buns()

        assert len(buns) == 3
        assert [bun.get_name() for bun in buns] == ['black bun', 'white bun', 'red bun']
        assert [bun.get_price() for bun in buns] == [100, 200, 300]

    def test_available_ingredients_returns_six_ingredients(self):
        database = Database()
        ingredients = database.available_ingredients()

        assert len(ingredients) == 6
        assert [i.get_name() for i in ingredients] == [
            'hot sauce', 'sour cream', 'chili sauce',
            'cutlet', 'dinosaur', 'sausage',
        ]
        assert [i.get_price() for i in ingredients] == [100, 200, 300, 100, 200, 300]
        assert [i.get_type() for i in ingredients] == [
            INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE,
            INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING,
        ]
