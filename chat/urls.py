from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.ChatConversationView.as_view())
]
