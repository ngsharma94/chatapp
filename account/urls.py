from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views
from rest_framework.routers import SimpleRouter

routeruser = SimpleRouter()
routeruser.register('user', views.SignUp)

urlpatterns = [
    path('', include(routeruser.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]