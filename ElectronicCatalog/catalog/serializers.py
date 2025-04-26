from rest_framework import serializers
from .models import Component
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'parent']


class CategoryDetailSerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()
    components = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'parent', 'subcategories', 'components']

    def get_subcategories(self, obj):
        children = obj.children.all()
        return CategorySerializer(children, many=True).data

    def get_components(self, obj):
        components = obj.components.all()
        return ComponentSerializer(components, many=True).data


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ['id', 'name', 'image_url', 'properties', 'category']


class ComponentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ['id', 'name', 'image_url', 'properties']
