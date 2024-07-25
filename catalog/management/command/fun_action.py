import json

from django.core.management import BaseCommand

from catalog.category.models import Category
from catalog.product.models import Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        '''получаем данные из фикстур с категориями'''
        with open('category_data.json', 'r') as file:
            file_json = json.load(file)
        return file_json

    @staticmethod
    def json_read_products():
        '''получаем данные из фикстурв с продуктами'''
        with open('product_data.json', 'r') as file:
            file_json = json.load(file)
        return file_json

    def handle(self, *args, **options):

        # Удалите все продукты
        Product.objects.all().delete()
        # Удалите все категории
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(id=category['fields']['pk'], name=category['fields']['name'],
                         description=category['fields']['description'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(name=product['fields']['name'], description=product['fields']['description'],
                        preview=product['fields']['preview'],
                        # получаем категорию из базы данных для корректной связки объектов
                        category=Category.objects.get(pk=product['fields']['category']),
                        price=product['fields']['price'], created_at=product['fields']['created_at'],
                        updated_at=product['fields']['updated_at'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)

