from django.db import models
from django.contrib.auth.models import User
from sheet.models import level


class userlevel(models.Model):
    select_user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    select_level = models.ForeignKey(
        level, on_delete=models.CASCADE, blank=True)
    level = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.user_name}/{self.level}'
