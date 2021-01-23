from django.contrib import admin
from .models import Recipe, Rating, Ingredient


# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'amount_of_calories']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['recipe', 'rate']
    list_filter = ['recipe']


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type_of_ingredient']
