from django.contrib.auth import password_validation, get_user_model
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=32, required=True)
    password1 = serializers.CharField(max_length=32, min_length=4, required=True)
    password2 = serializers.CharField(max_length=32, min_length=4, required=True)

    _error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
        "username_taken": _("The username was already taken.")
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._error_messages.update(self.default_error_messages)

    def validate_username(self, username):
        if (
                username
                and User.objects.filter(username__iexact=username).exists()
        ):
            raise serializers.ValidationError(self._error_messages["username_taken"])
        return username

    def validate(self, attrs):
        password1 = attrs.get('password1')
        password2 = attrs.get('password2')
        if password1 != password2:
            raise serializers.ValidationError(self._error_messages['password_mismatch'])

        password_validation.validate_password(password2)
        return attrs

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password2')
        user = User.objects.create_user(username, password=password)
        return user
