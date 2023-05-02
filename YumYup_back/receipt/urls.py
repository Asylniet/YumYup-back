from django.urls import path
from .views import *

urlpatterns = [
    path("list/", ReceiptAPIView.as_view()),
    path("list/ingredients/", IngredientAPIView.as_view()),
    path("list/ingredient_list/", ingredient_list),
    path("list/ingredient_list/<int:ingredient_list_id>/", ingredient_list_detail),
    path("list/ingredients/<int:ingredient_id>/", IngredientDetailAPIView.as_view()),
    path("list/<int:receipt_id>/", ReceiptDetailAPIView.as_view())
]
