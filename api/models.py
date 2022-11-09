from django.db import models


class Query(models.Model):
    query = models.CharField(max_length=1000)


class Student(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
