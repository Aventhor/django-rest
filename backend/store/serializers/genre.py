from rest_framework.serializers import ModelSerializer

from store.models import Genre


class GenreSerializer(ModelSerializer):

    class Meta:
        model = Genre
        fields = ['name']
