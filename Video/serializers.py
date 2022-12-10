from .models import Video, Comment, Category, SubCategory
from persiantools.jdatetime import JalaliDate
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    video = serializers.StringRelatedField(read_only=True, )
    created_at = serializers.SerializerMethodField(read_only=True)
    author = serializers.SlugRelatedField(read_only=True, slug_field='email')

    class Meta:
        model = Comment
        fields = '__all__'

    def get_created_at(self, obj):
        return JalaliDate(obj.created_at, locale=('fa')).strftime('%c')


class VideoSerializer(serializers.ModelSerializer):
    # SerializerMethodFields
    created_at = serializers.SerializerMethodField(read_only=True)
    updated_on = serializers.SerializerMethodField(read_only=True)
    # Relations
    publisher = serializers.SlugRelatedField(read_only=True, slug_field='email')
    category = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    comments = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Video
        fields = [
            'id', 'title', 'created_at', 'updated_on', 'publisher', 'time', 'is_active',
            'description', 'video', 'video_cover', 'category', 'comments'
        ]

    def get_created_at(self, obj):
        return JalaliDate(obj.created_at, locale=('fa')).strftime('%c')

    def get_updated_on(self, obj):
        return JalaliDate(obj.updated_on, locale=('fa')).strftime('%c')


class SubCategorySerializer(serializers.ModelSerializer):
    videos = serializers.StringRelatedField(many=True, read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'title', 'is_active', 'created_at', 'videos']

    def get_created_at(self, obj):
        return JalaliDate(obj.created_at, locale=('fa')).strftime('%c')


class CategorySerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField(read_only=True)
    subcategories = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'created_at', 'subcategories', ]

    def get_created_at(self, obj):
        return JalaliDate(obj.created_at, locale=('fa')).strftime('%c')
