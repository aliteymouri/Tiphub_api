from django.urls import path
from . import views

urlpatterns = [
    path('be_teacher', views.BeTeacherView.as_view(), name='be-teacher')
]
