from django.db import models
from django.contrib.auth.models import User


class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    __code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)

    def get_code(self):
        return self.__code

    def set_code(self, value):
        self.__code = value
