from django.contrib.auth import models


class User(models.User):
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

