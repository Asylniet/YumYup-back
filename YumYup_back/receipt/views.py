import json
from rest_framework.views import APIView
from .models import *
from rest_framework.decorators import api_view
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.response import Response
from .serializers import *


class ReceiptAPIView(APIView):
    def get(self, request):
        receipts = Receipt.objects.all()
        serializer = ReceiptSerializer(receipts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReceiptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReceiptDetailAPIView(APIView):
    def get_object(self, receipt_id):
        try:
            return Receipt.objects.get(pk=receipt_id)
        except Receipt.DoesNotExist as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, receipt_id):
        instance = self.get_object(receipt_id)
        serializer = ReceiptSerializer(instance)
        return Response(serializer.data)

    def put(self, request, receipt_id):
        receipt = self.get_object(receipt_id)
        data = json.loads(request.body)
        new_receipt_process = data.get('process', receipt.process)
        receipt.process = new_receipt_process
        receipt.save()
        serializer = ReceiptSerializer(receipt)
        return Response(serializer.data)

    def delete(self, request, receipt_id):
        instance = self.get_object(receipt_id)
        instance.delete()
        return JsonResponse({'deleted': True})


class IngredientAPIView(APIView):
    def get(self, request):
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IngredientDetailAPIView(APIView):
    def get_object(self, ingredient_id):
        try:
            return Ingredient.objects.get(pk=ingredient_id)
        except Ingredient.DoesNotExist as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, ingredient_id):
        instance = self.get_object(ingredient_id)
        serializer = IngredientSerializer(instance)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def ingredient_list(request):
    if request.method == 'GET':
        ingredients = Ingredient_list.objects.all()
        serializer = Ingredient_listSerializer(ingredients, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = Ingredient_listSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def ingredient_list_detail(request, ingredient_list_id):
    try:
        ingredient_lists = Ingredient_list.objects.get(id=ingredient_list_id)
    except Ingredient.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)
    if request.method == 'GET':
        serializer = Ingredient_listSerializer(ingredient_lists)
        return Response(serializer.data)

