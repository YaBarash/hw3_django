from django.db import models


class Category(models.Model):

    name = models.CharField(
        max_length=50,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    description = models.CharField(
        max_length=100,
        verbose_name="Описание",
        help_text="Введите  описание категории",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
