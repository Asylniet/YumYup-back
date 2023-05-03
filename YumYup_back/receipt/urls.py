from django.urls import path
from .views import *

urlpatterns = [
    path("list/", ReceiptAPIView.as_view()),
    path("list/<int:receipt_id>/", ReceiptDetailAPIView.as_view())
]
