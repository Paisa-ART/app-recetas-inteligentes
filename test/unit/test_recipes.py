import pytest
from django.test import TestCase
from django.contrib.auth.models import User
from recipes.models import Recipe, Ingredient, Step


class RecipeModelTests(TestCase):
    """Pruebas unitarias para el modelo Recipe"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.recipe = Recipe.objects.create(
            name='Fríjoles Tradicionales',
            description='Receta de fríjoles caseros',
            author=self.user,
            base_portions=4,
            prep_time=30,
            cook_time=90,
            difficulty='easy'
        )

    def test_recipe_creation(self):
        """Verifica que una receta se crea correctamente"""
        self.assertEqual(self.recipe.name, 'Fríjoles Tradicionales')
        self.assertEqual(self.recipe.author, self.user)
        self.assertEqual(self.recipe.base_portions, 4)

    def test_total_time_calculation(self):
        """Verifica que el tiempo total se calcula correctamente"""
        expected = self.recipe.prep_time + self.recipe.cook_time
        self.assertEqual(self.recipe.total_time, expected)

    def test_recipe_string_representation(self):
        """Verifica la representación en string de la receta"""
        self.assertEqual(str(self.recipe), 'Fríjoles Tradicionales')


class IngredientModelTests(TestCase):
    """Pruebas unitarias para el modelo Ingredient"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.recipe = Recipe.objects.create(
            name='Test Recipe',
            author=self.user,
            base_portions=4,
        )
        self.ingredient = Ingredient.objects.create(
            recipe=self.recipe,
            name='Fríjoles',
            quantity=2.0,
            unit='taza',
            cost=5000.00
        )

    def test_ingredient_creation(self):
        """Verifica que un ingrediente se crea correctamente"""
        self.assertEqual(self.ingredient.name, 'Fríjoles')
        self.assertEqual(self.ingredient.quantity, 2.0)
        self.assertEqual(self.ingredient.unit, 'taza')

    def test_cost_calculation_with_multiplier(self):
        """Verifica el cálculo de costo con multiplicador"""
        multiplier = 2.0
        expected_cost = 5000.00 * multiplier
        self.assertEqual(self.ingredient.get_cost(multiplier), expected_cost)


@pytest.mark.django_db
class PortionAdjustmentTests:
    """Pruebas para ajuste de porciones"""

    def test_portion_adjustment_calculation(self, django_db):
        """Verifica el cálculo de ajuste de porciones"""
        user = User.objects.create_user(username='test', password='test')
        recipe = Recipe.objects.create(
            name='Test',
            author=user,
            base_portions=4
        )
        Ingredient.objects.create(
            recipe=recipe,
            name='Ingredient',
            quantity=2.0,
            unit='taza',
            cost=1000.00
        )

        # Ajustar a 8 porciones (multiplicador = 2)
        multiplier = 8 / recipe.base_portions
        ingredient = recipe.ingredients.first()
        adjusted_quantity = ingredient.quantity * multiplier

        assert adjusted_quantity == 4.0
