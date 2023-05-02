import json

from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.response import Response
from django.db.models import Avg


@api_view(['GET', 'POST'])
def post(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'DELETE'])
def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return JsonResponse({'deleted': True})


@api_view(['GET', 'POST'])
def rating_comment(request, post_id):
    if request.method == 'GET':
        data = Rating.objects.all()
        ratings = data.filter(post_id=post_id)
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = RatingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'DELETE'])
def rating_comment_detail(request, post_id, rating_comment_id):
    try:
        rating_comment = Rating.objects.get(id=rating_comment_id, post_id=post_id)
    except Rating.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)
    if request.method == 'GET':
        serializer = RatingSerializer(rating_comment)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        rating_comment.delete()
        return JsonResponse({'deleted': True})


@api_view(['GET'])
def calculate_rating_by_post_id(request, post_id):
    data = Rating.objects.all()
    avg_rating = data.filter(post_id=post_id).aggregate(Avg('rating'))['rating__avg']
    return JsonResponse({'average_rating': avg_rating})


@api_view(['GET', 'POST'])
def saved_post(request):
    if request.method == 'GET':
        posts = Saved_post.objects.all()
        serializer = Saved_postSerializer(posts, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = Saved_postSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'DELETE'])
def saved_post_detail(request, saved_post_id):
    try:
        post = Saved_post.objects.get(id=saved_post_id)
    except Saved_post.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)
    if request.method == 'GET':
        serializer = Saved_postSerializer(post)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return JsonResponse({'deleted': True})


# Create your views here.
