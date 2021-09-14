from rest_framework.serializers import ModelSerializer

from store.models import Author


class AuthorSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'middle_name']
