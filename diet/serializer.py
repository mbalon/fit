from .models import Recipe, Ingredient, Rating
from rest_framework import serializers


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'category', 'ingredients', 'prep_time', 'amount_of_calories', 'describe', 'photo']


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'type_of_ingredient', 'cal_in_100_grams', 'carb_in_100_grams', 'protein_in_100_grams',
                  'fat_in_100_grams']


class RatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'recipe', 'rate']
