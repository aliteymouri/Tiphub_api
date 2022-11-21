from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

urlpatterns = [
    path('add/comment/<int:pk>', views.AddCommentView.as_view()),
    path('categories', views.CategoryListView.as_view()),
]

router = DefaultRouter()
router.register(r'videos', views.VideoViewSet, basename='videos')
router.register(r'comments', views.CommentViewSet, basename='comments')
urlpatterns += router.urls
