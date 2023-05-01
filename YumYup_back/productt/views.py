import json
from rest_framework.views import APIView
from productt.models import Product
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.response import Response
from productt.serializers import ProductSerializer


class ProductAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPIView(APIView):
    def get_object(self, product_id):
        try:
            return Product.objects.get(pk=product_id)
        except Product.DoesNotExist as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, product_id):
        instance = self.get_object(product_id)
        serializer = ProductSerializer(instance)
        return Response(serializer.data)

    def put(self, request, product_id):
        product = self.get_object(product_id)
        data = json.loads(request.body)
        new_product_name = data.get('name', product.name)
        new_product_date = data.get('expires_in', product.expires_in)
        product.name = new_product_name
        product.expires_in = new_product_date
        product.save()
        serializer = ProductSerializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)

    def delete(self, request, product_id):
        instance = self.get_object(product_id)
        instance.delete()
        return Response({'deleted': True})

# Create your views here.
