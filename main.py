import os

from views.line_models import Paragraph, ListItem, Heading, RecipeView
from scraper.parse_text import recipe_text_parser, main



if __name__ == '__main__':
    # Get new data using files in scraper dir
    # TBI

    # Load Already Saved Data
    # Converts data from .txt to dict wich can be saved as .json
    filepath = "data/recipes/funnel_cake_fries_recipe.txt"
    full_data = recipe_text_parser(filepath)

    recipe_view = RecipeView(full_data)

    print(recipe_view)


