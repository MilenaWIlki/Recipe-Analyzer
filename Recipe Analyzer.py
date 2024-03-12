class RecipeAnalyzer:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def analyze_recipe(self):
        return f"Recipe contains {len(self.ingredients)} ingredients"

# Example usage:
analyzer = RecipeAnalyzer()
analyzer.add_ingredient("Flour")
analyzer.add_ingredient("Sugar")
print(analyzer.analyze_recipe())
