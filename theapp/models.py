from django.db import models

class Service(models.Model):
    sname = models.CharField(max_length=64)
    surl = models.CharField(max_length=64)
    suser = models.CharField(max_length=64)
    spwd = models.CharField(max_length=64)
    sdb = models.CharField(max_length=64)
    ssrv = models.CharField(max_length=64)
    sprod = models.CharField(max_length=64)
