from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin, CreateModelMixin
from .models import ChatConversation, ChatCoversationUser
from .serializers import ChatConversationViewSerializer, ChatCoversationUserViewSerializer
from account.models import User
from account.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ChatConversationView(GenericAPIView, ListModelMixin, CreateModelMixin):
    def get_queryset(self):
        pk_user = User.objects.filter(phone_number = self.kwargs['pk'])
        receiver = pk_user.values()[0]['email']
        sender_user = User.objects.filter(email = self.request.user)
        sender = sender_user.values()[0]['email']
        return ChatConversation.objects.filter(sender__in=[receiver, sender], receiver__in=[receiver, sender])
    # queryset = ChatConversation.objects.all()
    serializer_class = ChatConversationViewSerializer

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        pk_user = User.objects.filter(phone_number = pk)
        if not pk_user:
            raise ValidationError('Incorrect Contact number')
        
        return self.list(request, pk)
    
    def post(self, request, pk):
        pk_user = User.objects.filter(phone_number = pk)
        if not pk_user:
            raise ValidationError('Incorrect Contact number')
        data = request.data
        serializer = ChatConversationViewSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        sender_user = User.objects.get(email = request.user)
        instance1, instance2 = serializer.save(user = request.user, user_type = 'S', sender = sender_user.email, receiver = pk_user.values()[0]['email'])
        instance2.user = User.objects.get(id = pk_user.values()[0]['id'])
        instance2.user_type = 'R'
        instance2.save()
        # serializer.save(user = request.user, user_type = 'S', sender = sender_user.email, receiver = pk_user.values()[0]['email'])
        return Response((ChatConversationViewSerializer(instance1).data, ChatConversationViewSerializer(instance2).data))
        # return Response(serializer.data)