from rest_framework import generics, permissions
from .models import Component
from .serializers import ComponentSerializer
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer, CategoryDetailSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.filter(parent__isnull=True)
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer



class ComponentListView(generics.ListAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer


class ComponentDetailView(generics.RetrieveAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer


class ComponentCreateView(generics.CreateAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    permission_classes = [permissions.IsAdminUser]


class ComponentUpdateView(generics.UpdateAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    permission_classes = [permissions.IsAdminUser]


class ComponentDeleteView(generics.DestroyAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    permission_classes = [permissions.IsAdminUser]
