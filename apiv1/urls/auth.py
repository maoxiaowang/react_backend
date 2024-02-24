from django.urls import path
from apiv1.views import auth as views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('whoami/', views.WhoAmI.as_view()),
    path('protected/', views.ExampleProtectedView.as_view(), name='protected_view'),
]
