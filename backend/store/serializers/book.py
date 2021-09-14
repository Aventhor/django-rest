from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django_filters.rest_framework import FilterSet, DateFilter
from decimal import Decimal

from store.models import Book
from store.models import Discount

class DiscountFilter(FilterSet):
    start_date = DateFilter(lookup_expr="gte")
    end_date = DateFilter(lookup_expr="lte")

    class Meta:
        model = Discount
        fields = [
            "start_date",
            "end_date",
        ]

class BookDiscountSerializer(ModelSerializer):

    filterset_class = DiscountFilter

    class Meta:
        model = Discount
        fields = ['amount']


class BookSerializer(ModelSerializer):

    discount = serializers.SerializerMethodField()
    price_with_discount = serializers.SerializerMethodField()

    def get_discount(self, obj):
        latest_discount = Discount.objects.filter(book=obj.id, is_active=True).last()
        return BookDiscountSerializer(latest_discount).data

    def get_price_with_discount(self, obj):
        discount = self.get_discount(obj)
        result = (Decimal(obj.price) - Decimal(discount['amount'])) 
        return "{:.2f}".format(result)


    class Meta:
        model = Book
        fields = ['sku', 'name', 'author', 'genres', 'publish_date', 'price', 'price_with_discount', 'discount']
