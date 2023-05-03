from rest_framework import serializers
from .models import *


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    receipt_id = serializers.PrimaryKeyRelatedField(queryset=Receipt.objects.all())
    date = serializers.DateField(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def create(self, validated_data):
        return Post.objects.create(**validated_data)


class RatingSerializer(serializers.Serializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    rating = serializers.FloatField()
    comment = serializers.CharField(max_length=5000)
    post_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    def create(self, validated_data):
        return Rating.objects.create(**validated_data)


class Saved_postSerializer(serializers.Serializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    post_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
