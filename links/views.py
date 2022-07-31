from django.shortcuts import render
from rest_framework import viewset


class PostCreateApi(viewset.CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostDetailApi(viewset.RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostUpdateApi(viewset.UpdateAPIView):
    queryset = Link.object.filter(active=True)
    serializer_class = LinkSerializer


class PostDeleteApi(viewset.DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

