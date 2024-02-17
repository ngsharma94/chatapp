from rest_framework import serializers
from .models import ChatCoversationUser, ChatConversation


class ChatCoversationUserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatCoversationUser
        fields = ['receiver',]

class ChatConversationViewSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    user_type = serializers.CharField(read_only=True)
    class Meta:
        model = ChatConversation
        fields = ['content', 'time', 'user', 'user_type']
    
    def create(self, validated_data):
        instance1 = ChatConversation.objects.create(**validated_data)
        instance2 = ChatConversation.objects.create(**validated_data)
        return instance1, instance2