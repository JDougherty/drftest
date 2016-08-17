from django.db import models

from rest_framework import serializers
from rest_framework_bulk import BulkListSerializer, BulkSerializerMixin, ListBulkCreateUpdateAPIView


class Foo(models.Model):
    name = models.CharField(max_length=20)
    class Meta:
        app_label = "foobar"


class FooSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta(object):
        model = Foo
        list_serializer_class = BulkListSerializer

class FooView(ListBulkCreateUpdateAPIView):
    queryset = Foo.objects.all()
    serializer_class = FooSerializer
