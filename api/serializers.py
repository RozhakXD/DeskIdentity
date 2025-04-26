from rest_framework import serializers

class UserAgentRequestSerializer(serializers.Serializer):
    os_type = serializers.CharField(required=True)
    browser = serializers.CharField(required=True)
    count = serializers.IntegerField(default=1, min_value=1, max_value=9999)
    unique = serializers.BooleanField(default=True)
