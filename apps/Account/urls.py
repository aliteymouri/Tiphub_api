from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    # Registeriation
    path('sign_up', views.SignUpView.as_view()),
    path('activate/<uidb64>/<token>', views.Activate.as_view(), name='activate'),

    path('users', views.UsersListView.as_view(),name='users_list'),
    path('logout', LogoutView.as_view(),name = 'logout'),
    path('edit_profile', views.EditProfileView.as_view(),name='edit_profile'),
    path('userpanel', views.UserPanelView.as_view(),name='userpanel'),
    path('change_password', views.ChangePasswordView.as_view(),name='change_password'),
    # Authentication
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
