from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
class UserProfile(models.Model):
    phone=models.CharField(verbose_name='Телефон', max_length=12)
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name="Профайл"
        verbose_name_plural="Профайл"
    def __str__(self):
        return f"{self.user.username}"