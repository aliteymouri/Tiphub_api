from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import VideoSerializer, CategorySerializer, CommentSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.generics import ListAPIView
from .models import Video, Category, Comment
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAdminOrReadOnly]

    def update(self, *args, **kwargs):
        instance = Video.objects.get(id=self.kwargs['pk'])
        ser = VideoSerializer(instance=instance, data=self.request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response('Video updated successfully', status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class AddCommentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        video = Video.objects.get(id=pk)
        ser = CommentSerializer(instance=video, data=request.data, partial=True)
        if ser.is_valid():
            Comment.objects.create(video=video, author=request.user, caption=request.data['caption'])
            return Response(F'Comment Added To {video.title} ', status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def list(self, request):
        queryset = Comment.objects.all()
        ser = CommentSerializer(instance=queryset, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        instance = Comment.objects.get(id=pk)
        ser = CommentSerializer(instance=instance, )
        return Response(ser.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        instance = Comment.objects.get(id=pk)
        instance.delete()
        return Response("Comment Deleted Successfully", status=status.HTTP_200_OK)


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
