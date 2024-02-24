import time

from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt import tokens
from rest_framework_simplejwt.views import (
    TokenObtainPairView as DRFTokenObtainPariView, TokenRefreshView as DRFTokenRefreshView
)


class Login(DRFTokenObtainPariView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # access_token = response.data["access"]
        # response.set_cookie(
        #     key=settings.SIMPLE_JWT["AUTH_COOKIE"],
        #     value=access_token,
        #     expires=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
        #     secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
        #     httponly=False,
        #     samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
        #     domain=settings.SIMPLE_JWT["AUTH_COOKIE_DOMAIN"],
        #     path=settings.SIMPLE_JWT["AUTH_COOKIE_PATH"]
        # )
        response.set_cookie('test', 'aaa', secure=False, domain='localhost', samesite=None, expires=1000)
        print(response.cookies)
        return response


class TokenRefreshView(DRFTokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if 'access' in response.data:
            access_token = response.data['access']

            # 更新令牌时，同时更新 HTTP Only Cookies 中的令牌
            response.set_cookie(key='access_token', value=access_token, httponly=True)

        return response


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        refresh_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'])
        token = tokens.RefreshToken(refresh_token)
        token.blacklist()

        response = Response()
        response.delete_cookie(settings.SIMPLE_JWT['AUTH_COOKIE_ACCESS'])
        response.delete_cookie(settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'])
        response.delete_cookie('X-CSRFToken')
        return response


class WhoAmI(APIView):

    def get(self, request):
        print(request.COOKIES)
        return Response()


class ExampleProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "This is a protected view"})
