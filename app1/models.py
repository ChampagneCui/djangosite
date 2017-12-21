from django.db import models


# Create your models here.
class Group(models.Model):
    name=models.CharField(max_length=20)

class Accounts(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=255)
    role=models.ForeignKey(Group,on_delete=models.CASCADE)

class Hosts(models.Model):
    hostname=models.CharField(max_length=20)
    ip=models.GenericIPAddressField()
    platform=models.CharField(max_length=20)
    description=models.CharField(max_length=255)

