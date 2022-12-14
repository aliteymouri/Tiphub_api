from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import VideoSerializer, CategorySerializer, CommentSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ViewSet, ModelViewSet
from .models import Video, Category, Comment, SubCategory
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Q


class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAdminOrReadOnly]

    def update(self, *args, **kwargs):
        instance = Video.objects.get(id=self.kwargs['pk'])
        ser = VideoSerializer(instance=instance, data=self.request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response('ویدیو با موفقیت بروزرسانی شد', status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CatDetailView(APIView):
    def get(self, req, **kwargs):
        sub = SubCategory.objects.get(pk=self.kwargs.get('pk'))
        videos = sub.videos.all()
        ser = VideoSerializer(instance=videos, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)


class AddCommentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        video = Video.objects.get(id=pk)
        ser = CommentSerializer(instance=video, data=request.data, partial=True)
        if ser.is_valid():
            Comment.objects.create(video=video, author=request.user, text=request.data['text'])
            return Response(F' نظر با موفقیت به {video.title} اضافه شد ', status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def list(self, request):
        queryset = Comment.objects.all()
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(queryset, request)
        ser = CommentSerializer(instance=page, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        instance = Comment.objects.get(id=pk)
        ser = CommentSerializer(instance=instance, )
        return Response(ser.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        instance = Comment.objects.get(id=pk)
        instance.delete()
        return Response("نظر با موفقیت حذف شد", status=status.HTTP_200_OK)


class SearchView(ListAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self):
        q = self.request.GET.get('q')
        return Video.objects.filter(Q(title__icontains=q) | Q(description__icontains=q))
