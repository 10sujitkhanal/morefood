# backends.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class AuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password) and user.is_restaurant_user or not user.is_staff:
            return user

        return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

    def has_permission(self, request):
        return request.user.is_active