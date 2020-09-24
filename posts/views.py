from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import serializers
from .models import Post, Comment
from .serializers import PostSerializer


class MyPaginationClass(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 255

class PostAPIView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = MyPaginationClass


    def get(self, request):


        article = Post.objects.all()
        serializer = PostSerializer(article, many=True)
        return Response({"article": serializer.data})



    def post(self, request):
        article = request.data.get('article')
        # print(type('type', article))
        serializer = PostSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"success": "OK"})


    def put(self, request, pk):
        saved_article = get_object_or_404(Post.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = PostSerializer(instance=saved_article, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"updated": "updated OK"})

    def delete(self, request, pk):
        article = get_object_or_404(Post.objects.all(), pk=pk)
        article.delete()
        return Response({"message": "ok"})

   

class CommentAPIView(viewsets.ModelViewSet):
    serializer_class = serializers.CommentsSerializer
    queryset = Comment.objects.all()
    pagination_class = MyPaginationClass


    def get(self, request):


        article = Comment.objects.all()
        serializer = serializers.CommentsSerializer(article, many=True)
        return Response({"article": serializer.data})



    def post(self, request):
        article = request.data.get('article')
        # print(type('type', article))
        serializer = serializers.CommentsSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"success": "OK"})



    def delete(self, request, pk):
        article = get_object_or_404(Comment.objects.all(), pk=pk)
        article.delete()
        return Response({"message": "ok"})
