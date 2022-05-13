import os
from line_models import Paragraph, ListItem, Heading, RecipeView
from parse_text import assign_line_data, main



if __name__ == '__main__':
    # Get Data from data/saved_recipe.json
    # Converts data from .txt to dict wich can be saved as .json
    full_data = main()

    recipe_view = RecipeView(full_data)

    print(recipe_view)


