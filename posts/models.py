# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.


class Post(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False, default='')
    content = models.TextField(blank=False, default='')
    author = models.ForeignKey('auth.User', related_name='posts',
                               on_delete=models.CASCADE)

    class Meta:
        ordering = ('creation_date',)
