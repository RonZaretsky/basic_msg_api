from rest_framework import serializers
from .models import MessageInfoItem
from django.contrib.auth.models import User



class MessageInfoItemSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(slug_field='username', queryset = User.objects.all())
    receivers = serializers.SlugRelatedField(slug_field='username', queryset = User.objects.all(), many = True)

    class Meta:
        model = MessageInfoItem
        fields = ['title','content','datetime_sent','sender','receivers']
        
    def create(self, validated_data):
        receivers_data = validated_data.pop('receivers')
        message_info = MessageInfoItem.objects.create(**validated_data)
        message_info.receivers.set(receivers_data)
        
        return message_info