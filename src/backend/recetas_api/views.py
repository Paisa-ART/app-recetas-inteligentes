from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request):
    """
    API Root - Welcome endpoint
    """
    return Response({
        'message': 'Bienvenido a App Recetas Inteligentes',
        'version': '1.0.0',
        'endpoints': {
            'admin': '/admin/',
            'auth': '/api/auth/',
            'recipes': '/api/recipes/',
        }
    })
