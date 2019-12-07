from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=20, verbose_name='密码')

    class Meta:
        db_table = 'user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    def to_dict(self):
        return {'id': self.id, 'username': self.username, 'password': self.password}
