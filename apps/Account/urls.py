from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    # Registeriation
    path('sign_up', views.SignUpView.as_view()),
    path('activate/<uidb64>/<token>', views.Activate.as_view(), name='activate'),

    path('users', views.UsersListView.as_view()),
    path('logout', views.LogoutView.as_view()),
    path('editprofile', views.EditProfileView.as_view()),
    path('userpanel', views.UserPanelView.as_view()),
    path('change_password', views.ChangePasswordView.as_view()),
    # Authentication
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
