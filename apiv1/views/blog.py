from rest_framework import generics

from apiv1.serializers.blog import ArticleSerializer, ArticleCreateUpdateSerializer
from common.views.mixins import CreateMixin, UpdateMixin
from main.models.blog import Article


class ListCreateArticleView(CreateMixin, generics.ListCreateAPIView):
    queryset = Article.objects.all()
    create_serializer_class = ArticleCreateUpdateSerializer
    serializer_class = ArticleSerializer


class RetrieveUpdateDestroyArticleView(UpdateMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    create_serializer_class = ArticleCreateUpdateSerializer
    serializer_class = ArticleSerializer
