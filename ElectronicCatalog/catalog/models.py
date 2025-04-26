from django.db import models
from django.contrib.postgres.fields import JSONField

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subcategories'
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Component(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='components'
    )
    name = models.CharField(max_length=255)
    image_url = models.URLField(blank=True)
    properties = models.JSONField()

    class Meta:
        verbose_name = "Component"
        verbose_name_plural = "Components"

    def __str__(self):
        return self.name
