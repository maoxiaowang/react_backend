from django.urls import path, include

urlpatterns = [
    path('auth/', include('apiv1.urls.auth')),
    path('blog/', include('apiv1.urls.blog'))
]
