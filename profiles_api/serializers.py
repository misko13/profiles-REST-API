from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializers a neme field for testing our APIViea , similar to django Forms"""
    name = serializers.CharField(max_length=10)
