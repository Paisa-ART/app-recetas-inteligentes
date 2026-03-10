from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Recipe(models.Model):
    """
    Modelo de Receta
    """
    DIFFICULTY_CHOICES = [
        ('easy', 'Fácil'),
        ('medium', 'Media'),
        ('hard', 'Difícil'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    base_portions = models.IntegerField(default=4, validators=[MinValueValidator(1)])
    
    # Tiempos en minutos
    prep_time = models.IntegerField(default=0, help_text="Tiempo de preparación en minutos")
    cook_time = models.IntegerField(default=0, help_text="Tiempo de cocción en minutos")
    
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='easy')
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    @property
    def total_time(self):
        """Total de tiempo de preparación y cocción"""
        return self.prep_time + self.cook_time


class Ingredient(models.Model):
    """
    Modelo de Ingrediente
    """
    UNIT_CHOICES = [
        ('g', 'gramos'),
        ('kg', 'kilogramos'),
        ('ml', 'mililitros'),
        ('l', 'litros'),
        ('taza', 'taza'),
        ('cuchara', 'cuchara'),
        ('unidad', 'unidad'),
        ('pinch', 'pizca'),
    ]

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=200)
    quantity = models.FloatField(validators=[MinValueValidator(0.1)])
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0, 
                               help_text="Precio unitario estándar")

    def __str__(self):
        return f"{self.quantity} {self.unit} de {self.name}"

    def get_cost(self, portions_multiplier):
        """Calcula el costo según el multiplicador de porciones"""
        return float(self.cost) * portions_multiplier


class Step(models.Model):
    """
    Modelo de Paso en la preparación
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='steps')
    order = models.IntegerField()
    description = models.TextField()
    duration = models.IntegerField(default=0, help_text="Duración en minutos")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Paso {self.order}: {self.recipe.name}"


class ShoppingList(models.Model):
    """
    Modelo de Lista de Compras generada
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='shopping_lists')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shopping_lists')
    portions = models.IntegerField(validators=[MinValueValidator(1)])
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    generated_at = models.DateTimeField(auto_now_add=True)
    ingredients_data = models.JSONField(default=dict)

    def __str__(self):
        return f"Lista de {self.recipe.name} - {self.portions} porciones"


class FavoriteRecipe(models.Model):
    """
    Modelo de Recetas Favoritas
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_recipes')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='favorited_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'recipe']

    def __str__(self):
        return f"{self.user.username} - {self.recipe.name}"
