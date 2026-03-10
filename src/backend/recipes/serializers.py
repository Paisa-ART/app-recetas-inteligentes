from rest_framework import serializers
from .models import Recipe, Ingredient, Step, ShoppingList, FavoriteRecipe


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'quantity', 'unit', 'cost']


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['id', 'order', 'description', 'duration']


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    steps = StepSerializer(many=True, read_only=True)
    author_name = serializers.CharField(source='author.get_full_name', read_only=True)
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = [
            'id', 'name', 'description', 'author', 'author_name', 'base_portions',
            'prep_time', 'cook_time', 'total_time', 'difficulty', 'image',
            'created_at', 'updated_at', 'is_public', 'ingredients', 'steps',
            'is_favorite'
        ]

    def get_is_favorite(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return FavoriteRecipe.objects.filter(
                user=request.user,
                recipe=obj
            ).exists()
        return False


class RecipeCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'name', 'description', 'base_portions', 'prep_time',
            'cook_time', 'difficulty', 'image', 'is_public'
        ]


class AdjustedRecipeSerializer(serializers.Serializer):
    """
    Serializer para receta ajustada según número de porciones
    """
    portions = serializers.IntegerField(min_value=1)

    def to_representation(self, instance):
        recipe = instance['recipe']
        portions = instance['portions']
        multiplier = portions / recipe.base_portions

        adjusted_ingredients = []
        total_cost = 0

        for ingredient in recipe.ingredients.all():
            adjusted_qty = ingredient.quantity * multiplier
            ingredient_cost = ingredient.get_cost(multiplier)
            total_cost += ingredient_cost

            adjusted_ingredients.append({
                'id': ingredient.id,
                'name': ingredient.name,
                'quantity': round(adjusted_qty, 2),
                'unit': ingredient.unit,
                'cost': float(ingredient_cost)
            })

        return {
            'recipe': RecipeSerializer(recipe, context=self.context).data,
            'portions': portions,
            'multiplier': round(multiplier, 2),
            'adjusted_ingredients': adjusted_ingredients,
            'total_cost': round(total_cost, 2),
        }


class ShoppingListSerializer(serializers.ModelSerializer):
    recipe_name = serializers.CharField(source='recipe.name', read_only=True)

    class Meta:
        model = ShoppingList
        fields = [
            'id', 'recipe', 'recipe_name', 'portions', 'total_cost',
            'generated_at', 'ingredients_data'
        ]


class FavoriteRecipeSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer(read_only=True)

    class Meta:
        model = FavoriteRecipe
        fields = ['id', 'recipe', 'added_at']
