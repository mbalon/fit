from django.urls import include,path
from rest_framework import routers
from .views import RecipeViewSet, RatingViewSet,IngredientViewSet

router = routers.DefaultRouter()
router.register(r'recipe', RecipeViewSet)
router.register(r'rating', RatingViewSet)
router.register(r'ingredient', IngredientViewSet)

urls_pattern = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'), namespace='rest_framework')
]