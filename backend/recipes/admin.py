from django.contrib import admin

from .models import (FavoriteRecipe, Follow, Ingredient, IngredientRecipe,
                     Recipe, ShoppingCart, Tag)

ERROR_MESSAGE = 'empty'


class RecipeIngredientAdmin(admin.StackedInline):
    model = IngredientRecipe
    autocomplete_fields = ('ingredient',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'get_author', 'name', 'text',
        'cooking_time', 'get_tags', 'get_ingredients',
        'pub_date', 'get_favorite_count')
    search_fields = (
        'name', 'cooking_time',
        'author__email', 'ingredients__name')
    list_filter = ('pub_date', 'tags',)
    inlines = (RecipeIngredientAdmin,)
    empty_value_display = ERROR_MESSAGE

    @admin.display(
        description='mail_author')
    def get_author(self, obj):
        return obj.author.email

    @admin.display(description='tags')
    def get_tags(self, obj):
        list_ = [_.name for _ in obj.tags.all()]
        return ', '.join(list_)

    @admin.display(description='ingredients')
    def get_ingredients(self, obj):
        return '\n '.join([
            f'{item["ingredient__name"]} - {item["amount"]}'
            f' {item["ingredient__measurement_unit"]}.'
            for item in obj.recipe.values(
                'ingredient__name',
                'amount', 'ingredient__measurement_unit')])

    @admin.display(description='Содержится в избранном')
    def get_favorite_count(self, obj):
        return obj.in_favorite.count()


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'color', 'slug',)
    search_fields = ('name', 'slug',)
    empty_value_display = ERROR_MESSAGE


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'measurement_unit',)
    search_fields = (
        'name', 'measurement_unit',)
    empty_value_display = ERROR_MESSAGE


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'author', 'created',)
    search_fields = (
        'user__email', 'author__email',)
    empty_value_display = ERROR_MESSAGE


@admin.register(FavoriteRecipe)
class FavoriteRecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'recipe')
    empty_value_display = ERROR_MESSAGE


@admin.register(ShoppingCart)
class SoppingCartAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'recipe',)
    empty_value_display = ERROR_MESSAGE
