from django.urls import path
from . import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'account'
urlpatterns = [
    path('users', views.UsersListView.as_view()),
    path('logout', views.LogoutView.as_view()),
    # Authentication
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
