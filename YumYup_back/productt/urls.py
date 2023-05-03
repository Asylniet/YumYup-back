from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("list/", ProductAPIView.as_view()),
    path("expiring_products/", get_expiring_products),
    path("list/<int:product_id>/", ProductDetailAPIView.as_view())
]
