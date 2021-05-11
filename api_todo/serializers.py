from rest_framework.serializers import ModelSerializer

from . import models


class TodoSerializer(ModelSerializer):
    """ Todo api, serializer class  """

    class Meta:
        model = models.Todo
        fields = "__all__"
        read_only_fields = ["id"]
