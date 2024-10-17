from django.shortcuts import render

from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if self.request.user == self.get_object().author:
            serializer.save()

    def perform_destroy(self, instance):
        if self.request.user == instance.author:
            instance.delete()
