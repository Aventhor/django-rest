from rest_framework.serializers import ModelSerializer

from store.models import Discount


class DiscountSerializer(ModelSerializer):

    class Meta:
        model = Discount
        fields = ['book', 'start_date', 'end_date', 'amount']
