from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=200)
    detail = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, max_length=50, default='', related_name="user1")
    assigned_to_user = models.ForeignKey(User, max_length=50, default='', related_name="userm")
    date = models.DateTimeField(auto_now_add=True, )
    date_off = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.name
