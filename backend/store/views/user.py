from rest_framework.mixins import CreateModelMixin
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import OrderingFilter

from store.models import User
# from store.serializers import FeedbackSerializer


class UserView(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
   # serializer_class = FeedbackSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
