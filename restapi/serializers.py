from rest_framework import serializers

class ComputerHardwareSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=100, required=False)
    price = serializers.IntegerField(required=False)
