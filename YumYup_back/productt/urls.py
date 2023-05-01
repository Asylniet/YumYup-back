from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("list/", ProductAPIView.as_view()),
    path("list/<int:product_id>/", ProductDetailAPIView.as_view())
]
