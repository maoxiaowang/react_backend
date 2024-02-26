from rest_framework import serializers

from apiv1.serializers import UserSerializer
from main.models.blog import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Article
        fields = '__all__'


class ArticleCreateUpdateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Article
        fields = ('title', 'content', 'author')
