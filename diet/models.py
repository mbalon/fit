from django.db import models


RATE = (
    ("0", "horrible"),
    ("1", "disgusting"),
    ("2", "definitely not good"),
    ("3", "not so bad"),
    ("4", "really good"),
    ("5", "astonish")
)

INGREDIENTS_TYPES = (
    ("veg", 'vegetable'),
    ('ft', 'fruit'),
    ('mt', 'meat'),
    ('fh', 'fish'),
    ('dy', 'diary'),
    ('egg', 'eggs'),
    ('or', 'other')
)
# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    ingredients = models.TextField()
    prep_time = models.CharField(max_length=30)
    amount_of_calories = models.IntegerField(default=0)
    describe = models.TextField()
    photo = models.FileField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rate = models.CharField(max_length=255, choices=RATE, default='0')


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    type_of_ingredient = models.CharField(max_length=255, choices=INGREDIENTS_TYPES, default='or')
    cal_in_100_grams = models.IntegerField()
    carb_in_100_grams = models.FloatField()
    protein_in_100_grams = models.FloatField()
    fat_in_100_grams = models.FloatField()
