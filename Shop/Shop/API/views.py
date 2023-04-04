from django.shortcuts import render
from rest_framework import viewsets, decorators
from rest_framework.response import Response
from .serializers import *
from Main.models import Flowers


# Create your views here.

class FlowersAPIView(viewsets.ModelViewSet):
    queryset = Flowers.objects.all()
    serializer_class = FlowersSerializer