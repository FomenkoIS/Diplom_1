import pytest
from unittest.mock import Mock
from bun import Bun
from burger import Burger
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE
from ingredient_types import INGREDIENT_TYPE_FILLING


@pytest.fixture
def burger():
    return Burger()

class TestBurger:

    BUNS = [
        ("Флюоресцентная булка R2-D3", 988),
        ("Краторная булка N-200i", 1255)
    ]


    INGREDIENTS_SAUCES = [
        (INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90),
        (INGREDIENT_TYPE_SAUCE, "Соус фирменный Space Sauce", 80),
        (INGREDIENT_TYPE_SAUCE, "Соус традиционный галактический", 15),
        (INGREDIENT_TYPE_SAUCE, "Соус с шипами Антарианского плоскоходца", 88)
    ]

    INGREDIENTS_FILLING = [
        (INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков Protostomia", 1337),
        (INGREDIENT_TYPE_FILLING, "Говяжий метеорит (отбивная)", 3000),
        (INGREDIENT_TYPE_FILLING, "Биокотлета из марсианской Магнолии", 424),
        (INGREDIENT_TYPE_FILLING, "Филе Люминесцентного тетраодонтимформа", 988),
        (INGREDIENT_TYPE_FILLING, "Хрустящие минеральные кольца", 300),
        (INGREDIENT_TYPE_FILLING, "Плоды Фалленианского дерева", 874),
        (INGREDIENT_TYPE_FILLING, "Кристаллы марсианских альфа-сахаридов", 762),
        (INGREDIENT_TYPE_FILLING, "Мини-салат Экзо-Плантаго", 4400),
        (INGREDIENT_TYPE_FILLING, "Сыр с астероидной плесенью", 4142)
    ]

    ALL_INGREDIENTS = INGREDIENTS_SAUCES + INGREDIENTS_FILLING  

    @pytest.mark.parametrize("bun_name, bun_price", BUNS)
    def test_set_buns_set_buns_correct(self, bun_name, bun_price, burger):

        my_bun = Bun(bun_name, bun_price)

        burger.set_buns(my_bun)

        assert burger.bun == my_bun


    @pytest.mark.parametrize("bun_name, bun_price", BUNS)
    def test_set_buns_name_check(self, bun_name, bun_price, burger):
            
            my_bun = Bun(bun_name, bun_price)
    
            burger.set_buns(my_bun)
    
            assert burger.bun.get_name() == bun_name


    @pytest.mark.parametrize("bun_name, bun_price", BUNS)
    def test_set_buns_price_check(self, bun_name, bun_price, burger):
            
            my_bun = Bun(bun_name, bun_price)
    
            burger.set_buns(my_bun)
    
            assert burger.bun.get_price() == bun_price



    @pytest.mark.parametrize("ingredient_type, name, price", ALL_INGREDIENTS)
    def test_add_ingredient_added_success(self, ingredient_type, name, price, burger):

        my_ingredient = Ingredient(ingredient_type, name, price)

        burger.add_ingredient(my_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == my_ingredient



    @pytest.mark.parametrize("ingredient_type, name, price", ALL_INGREDIENTS)
    def test_add_ingredient_type_check(self, ingredient_type, name, price, burger):
        
        my_ingredient = Ingredient(ingredient_type, name, price)
        
        burger.add_ingredient(my_ingredient)
        
        assert burger.ingredients[0].get_type() == ingredient_type


    @pytest.mark.parametrize("ingredient_type, name, price", ALL_INGREDIENTS)
    def test_add_ingredient_name_check(self, ingredient_type, name, price, burger):
    
        my_ingredient = Ingredient(ingredient_type, name, price)
    
        burger.add_ingredient(my_ingredient)
    
        assert burger.ingredients[0].get_name() == name


    @pytest.mark.parametrize("ingredient_type, name, price", ALL_INGREDIENTS)
    def test_add_ingredient_price_check(self, ingredient_type, name, price, burger):
        
        my_ingredient = Ingredient(ingredient_type, name, price)
        
        burger.add_ingredient(my_ingredient)
        
        assert burger.ingredients[0].get_price() == price

    def test_add_ingredient_add_two_ingrediets(self, burger):

        my_ingredient_1 = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90)
        my_ingredient_2 = Ingredient(INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков Protostomia", 1337)

        burger.add_ingredient(my_ingredient_1)
        burger.add_ingredient(my_ingredient_2)


        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == my_ingredient_1
        assert burger.ingredients[1] == my_ingredient_2




    
