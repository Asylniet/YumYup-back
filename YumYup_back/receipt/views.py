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

