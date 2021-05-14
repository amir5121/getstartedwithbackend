from django.db import models


class Addressbook(models.Model):
    phone_num = models.CharField(max_length=11)
    name = models.CharField(max_length=256)
