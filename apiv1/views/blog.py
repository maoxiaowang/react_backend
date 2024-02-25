from rest_framework import viewsets

from apiv1.serializers.blog import ArticleSerializer
from main.models.blog import Article


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = []
