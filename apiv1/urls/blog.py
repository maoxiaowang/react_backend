from django.urls import path
from apiv1.views import blog as views

urlpatterns = [
    path('articles/', views.ListCreateArticleView.as_view(), name='articles'),
    path('article/<int:pk>/', views.RetrieveUpdateDestroyArticleView.as_view(), name='article'),
]
