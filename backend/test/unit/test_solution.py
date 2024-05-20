import pytest
from src.controllers.recipecontroller import RecipeController
from unittest.mock import patch, MagicMock
from src.static.diets import Diet

@pytest.mark.unit
@pyest.mark.parametrize("take_best, diet, returned_recipe_dict", [(True, True, True, False, False, False), (Diet.VEGETARIAN, Diet.VEGAN, Diet.NORMAL )
                                                                   ({"0.2": 'Banana Bread', "0.1": "Pancakes", "0.1": "Whole Grain Bread"},
                                                                                                        {"0,2": "Whole Grain Bread"}, {"0.2": 'Banana Bread', "0.1": "Pancakes", "0.1": "Whole Grain Bread"},
                                                                                                        {}, {})])
# The dictionaries have been chosen as if the diets were "vegetarian", "vegan", and "normal".
def test_get_recipe(take_best, diet, returned_recipe_dict):
    recipe_controller = RecipeController()

    mock_get_readiness_of_recipes = MagicMock(return_value = returned_recipe_dict)

    with patch.object(RecipeController, 'get_readiness_of_recipes', mock_get_readiness_of_recipes):
        # Call the get_recipe method
        result = recipe_controller.get_recipe(take_best, diet)
        assert result != None 


