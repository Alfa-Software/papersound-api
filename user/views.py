from rest_framework import viewsets, generics
from .models import User
from .serializer import UserSerializer

class Userviewset(viewsets.ModelViewSet):
    queryset=User.objects.all()
    page_size = 10
    serializer_class = UserSerializer