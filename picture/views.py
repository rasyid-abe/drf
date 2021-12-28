from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PictureSerializer
from .models import Picture
from rest_framework import permissions, generics
from .permissions import IsOwner
from rest_framework.parsers import FormParser, MultiPartParser
# Create your views here.

class PictureListAPIView(ListCreateAPIView):
    serializer_class = PictureSerializer
    parser_classes = (FormParser, MultiPartParser)
    queryset = Picture.objects.all()
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class PictureDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PictureSerializer
    parser_classes = (FormParser, MultiPartParser)
    queryset = Picture.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    lookup_field = 'id'

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
