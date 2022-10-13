from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Painting

# Create your views here.


class MainView(APIView):

    def get(self, request):
        return Response({})

class PaintingView(APIView):

    def get(self, request):
        painting_obj = Painting.objects.get(id=1)
        return Response(model_to_dict(painting_obj))