from rest_framework import generics, permissions
from .models import Component, Category
from .serializers import(
    ComponentSerializer,
    CategorySerializer,
    CategoryDetailSerializer,
    ComponentListSerializer,
)
from .filters import ComponentFilter
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

class CategoryComponentListView(generics.ListAPIView):
    serializer_class = ComponentListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ComponentFilter
    search_fields = ['name']

    def get_queryset(self):
        category_id = self.kwargs['pk']
        return Component.objects.filter(category_id=category_id)


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
