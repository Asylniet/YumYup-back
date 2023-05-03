import json

import status
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_jwt.utils import jwt_encode_handler
from datetime import datetime, timedelta
from .serializers import *


class SignInView(APIView):
    def post(self, request):
        eml = request.data.get('email')
        psd = request.data.get('password')

        user = User.objects.filter(email=eml).first()
        if not user or not check_password(psd, user.password):
            return Response({'error': 'Invalid credentials'})
        token = jwt_encode_handler(
            {'user_id': user.pk, 'exp_time': int((datetime.now() + timedelta(days=1)).timestamp())})
        return Response({
            'token': str(token),
            'id': user.id,
        })


class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            existing_user = User.objects.filter(email=request.data['email']).exists()
            if existing_user:
                return Response({'error': 'Username already taken. Please choose a different username.'}, status=400)
            password = make_password(request.data['password']) # hash the password
            user = serializer.save(password=password)
            token = jwt_encode_handler(
                {'user_id': user.pk, 'exp_time': int((datetime.now() + timedelta(days=1)).timestamp())})

            return Response({
                'token': str(token),
                'id': user.id,
            })

        return Response(serializer.errors, status=400)


class ProfileDetailAPIView(APIView):
    def get_object(self, profile_id):
        try:
            return Profile.objects.get(pk=profile_id)
        except Profile.DoesNotExist as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, profile_id):
        instance = self.get_object(profile_id)
        serializer = ProfileSerializer(instance)
        return Response(serializer.data)

    def put(self, request, profile_id):
        profile = self.get_object(profile_id)
        data = json.loads(request.body)
        new_phone_number = data.get('phone_number', profile.phone_number)
        new_bio = data.get('bio', profile.bio)
        new_avatar = data.get('avatar', profile.avatar)
        profile.phone_number = new_phone_number
        profile.bio = new_bio
        profile.avatar = new_avatar
        profile.save()
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def delete(self, request, profile_id):
        instance = self.get_object(profile_id)
        instance.delete()
        return JsonResponse({'deleted': True})

