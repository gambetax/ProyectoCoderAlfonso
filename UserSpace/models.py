from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    class Meta:
        db_table = 'userspace_avatar'