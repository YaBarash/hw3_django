import datetime

from django.db import models
from category.models import Category


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.CharField(
        max_length=100,
        verbose_name="Описание",
        help_text="Введите описание продукта",
        null=True,
        blank=True,
    )
    preview = models.ImageField(
        upload_to="product/preview",
        verbose_name="Фото",
        help_text="Прикрепите фото",
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        null=True,
        blank=True,
        related_name="product",
    )
    price = models.IntegerField(
        verbose_name="Цена",
        null=True,
        blank=True,
    )
    created_at = models.DateField(
        verbose_name="Дата создания",
        auto_now_add=True,
        null=True,
        blank=True,
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения",
        null=True,
        blank=True,
    )


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price", "category"]

    def __str__(self):
        return self.name
