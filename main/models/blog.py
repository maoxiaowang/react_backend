from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=65535)
    author = models.ForeignKey(User, models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'main_blog_article'
        ordering = ('-id',)


class ArticleComment(models.Model):
    content = models.TextField(max_length=2048)
    article = models.ForeignKey(Article, models.CASCADE)
    user = models.ForeignKey(User, models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'main_blog_article_comment'
        ordering = ('-id',)
