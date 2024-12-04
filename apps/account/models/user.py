from django.contrib.auth.models import AbstractUser
from django.db import models

from safedelete import SOFT_DELETE
from safedelete.models import SafeDeleteMixin


class User(AbstractUser, SafeDeleteMixin):

    _safedelete_policy = SOFT_DELETE

    REQUIRED_FIELDS = ["name", "phone_number"]

    name = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=50, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def activate(self, method):
        if method == "POST":
            self.is_active = True
        elif method == "DELETE":
            self.is_active = False
        else:
            pass
        self.save()

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username
