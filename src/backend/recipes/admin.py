from django.contrib import admin
from .models import Recipe, Ingredient, Step, ShoppingList, FavoriteRecipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'difficulty', 'base_portions', 'created_at']
    search_fields = ['name', 'description']
    list_filter = ['difficulty', 'created_at', 'is_public']


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'recipe', 'quantity', 'unit', 'cost']
    search_fields = ['name', 'recipe__name']


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ['order', 'recipe', 'duration']
    search_fields = ['recipe__name']


@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ['recipe', 'user', 'portions', 'total_cost', 'generated_at']
    search_fields = ['recipe__name', 'user__username']


@admin.register(FavoriteRecipe)
class FavoriteRecipeAdmin(admin.ModelAdmin):
    list_display = ['user', 'recipe', 'added_at']
    search_fields = ['user__username', 'recipe__name']
