from rest_framework import serializers
from . import models

class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    body = serializers.CharField(required=False, allow_blank=True, max_length=100)


    def create(self, validated_data):
        return models.Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance

    class Meta:
        model = models.Post
        fields = ('id', 'body', 'owner')
