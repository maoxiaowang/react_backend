from django.urls import path
from apiv1.views import blog as views

urlpatterns = [
    path('articles/', views.ArticleViewSet.as_view({'get': 'list'}))
]
