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
from django.db.models import Q
from django.db.models import Value, F, FloatField, Textfield
from django.db.models.functions import Cast


class CategoryComponentListView(generics.ListAPIView):
    serializer_class = ComponentListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ComponentFilter
    search_fields = ['name']
    ordering_fields = ['id', 'name']  # Allow ordering by id, name by default

    def get_queryset(self):
        category_id = self.kwargs['pk']
        queryset = Component.objects.filter(category_id=category_id)

        # --- Custom filtering by properties ---
        properties_filters = {}
        for key, value in self.request.query_params.items():
            if key.startswith('prop__'):
                prop_key = key.split('prop__', 1)[1]
                properties_filters[prop_key] = value

        if properties_filters:
            for prop_key, prop_value in properties_filters.items():
                queryset = queryset.filter(
                    Q(**{f"properties__{prop_key}__icontains": prop_value})
                )

        # --- Custom sorting by property ---
        ordering = self.request.query_params.get('ordering')
        if ordering:
            if ordering.startswith('prop__') or ordering.startswith('-prop__'):
                desc = ordering.startswith('-')
                prop_field = ordering.lstrip('-').split('prop__', 1)[1]

                # Annotate the property value so we can order by it
                queryset = queryset.annotate(
                    prop_value=Cast(
                        F(f"properties__{prop_field}"),
                        output_field=TextField()  # or FloatField() if you know it’s numeric
                    )
                )

                # Order by annotated field
                if desc:
                    queryset = queryset.order_by('-prop_value')
                else:
                    queryset = queryset.order_by('prop_value')

        return queryset


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
