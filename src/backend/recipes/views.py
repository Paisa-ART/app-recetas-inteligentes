from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .models import Recipe, Ingredient, Step, ShoppingList, FavoriteRecipe
from .serializers import (
    RecipeSerializer, RecipeCreateUpdateSerializer, AdjustedRecipeSerializer,
    ShoppingListSerializer, FavoriteRecipeSerializer
)


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API para gestionar recetas
    """
    queryset = Recipe.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return RecipeCreateUpdateSerializer
        return RecipeSerializer

    def get_queryset(self):
        queryset = Recipe.objects.all()
        if self.request.query_params.get('my_recipes'):
            queryset = queryset.filter(author=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def adjust_portions(self, request, pk=None):
        """
        Ajusta los ingredientes según el número de porciones
        """
        recipe = self.get_object()
        serializer = AdjustedRecipeSerializer(
            {'recipe': recipe, 'portions': request.data.get('portions')},
            context={'request': request}
        )
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def generate_shopping_list(self, request, pk=None):
        """
        Genera una lista de compras para la receta
        """
        recipe = self.get_object()
        portions = request.data.get('portions', recipe.base_portions)

        multiplier = portions / recipe.base_portions
        ingredients_data = []
        total_cost = 0

        for ingredient in recipe.ingredients.all():
            adjusted_qty = ingredient.quantity * multiplier
            ingredient_cost = ingredient.get_cost(multiplier)
            total_cost += ingredient_cost

            ingredients_data.append({
                'name': ingredient.name,
                'quantity': round(adjusted_qty, 2),
                'unit': ingredient.unit,
                'cost': float(ingredient_cost)
            })

        shopping_list = ShoppingList.objects.create(
            recipe=recipe,
            user=request.user,
            portions=portions,
            total_cost=total_cost,
            ingredients_data=ingredients_data
        )

        serializer = ShoppingListSerializer(shopping_list)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post', 'delete'])
    def favorite(self, request, pk=None):
        """
        Agregar o remover receta de favoritas
        """
        recipe = self.get_object()

        if request.method == 'POST':
            favorite, created = FavoriteRecipe.objects.get_or_create(
                user=request.user,
                recipe=recipe
            )
            serializer = FavoriteRecipeSerializer(favorite)
            status_code = status.HTTP_201_CREATED if created else status.HTTP_200_OK
            return Response(serializer.data, status=status_code)

        elif request.method == 'DELETE':
            FavoriteRecipe.objects.filter(
                user=request.user,
                recipe=recipe
            ).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'])
    def favorites(self, request):
        """
        Obtener recetas favoritas del usuario
        """
        favorites = FavoriteRecipe.objects.filter(user=request.user)
        serializer = FavoriteRecipeSerializer(favorites, many=True)
        return Response(serializer.data)


class ShoppingListViewSet(viewsets.ModelViewSet):
    """
    API para gestionar listas de compras generadas
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ShoppingListSerializer

    def get_queryset(self):
        return ShoppingList.objects.filter(user=self.request.user)

    @action(detail=True, methods=['get'])
    def export_pdf(self, request, pk=None):
        """
        Exportar lista de compras a PDF
        """
        shopping_list = self.get_object()
        return Response({
            'message': 'PDF generation pending',
            'shopping_list': ShoppingListSerializer(shopping_list).data
        })
