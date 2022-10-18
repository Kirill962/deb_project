from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (AddAndDeleteSubscribe, AddDeleteFavoriteRecipe,
                       AddDeleteShoppingCart, AuthToken, IngredientsViewSet,
                       RecipesViewSet, TagsViewSet, UsersViewSet, set_password)

app_name = 'api'

router = DefaultRouter()
router.register('users', UsersViewSet)
router.register('tags', TagsViewSet)
router.register('ingredients', IngredientsViewSet)
router.register('recipes', RecipesViewSet)


urlpatterns = [
     path(
          'auth/token/login/',
          AuthToken.as_view()),
     path(
          'users/set_password/',
          set_password),
     path(
          'users/<int:user_id>/subscribe/',
          AddAndDeleteSubscribe.as_view()),
     path(
          'recipes/<int:recipe_id>/favorite/',
          AddDeleteFavoriteRecipe.as_view()),
     path(
          'recipes/<int:recipe_id>/shopping_cart/',
          AddDeleteShoppingCart.as_view()),
     path('', include(router.urls)),
     path('', include('djoser.urls')),
     path('auth/', include('djoser.urls.authtoken')),
]