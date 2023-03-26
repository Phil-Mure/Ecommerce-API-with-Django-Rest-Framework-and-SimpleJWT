from user.models import User
from rest_framework import viewsets
from .serializer import UserSerializer
from django.http import HttpResponse
from rest_framework import permissions
from api.permissions import IsUserOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all() 
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


def home(request):
    return HttpResponse('To start accessing the API, pass some parameters into the url such as http://127.0.0.1:8000/api/')