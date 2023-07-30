import datetime

from django.db import models

# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length=400)
    age = models.IntegerField()
    favorite_book = models.CharField(max_length=1024)

class FormModel(models.Model):
    name = models.CharField(max_length=48)


class FormField(models.Model):
    form = models.ForeignKey(FormModel, related_name="form_fields", on_delete=models.CASCADE)
    name = models.CharField(max_length=48)
    label = models.CharField(max_length=48)
    type = models.CharField(max_length=48)


class FormRecord(models.Model):
    date = models.DateTimeField(null=True)



class FormData(models.Model):
    record_id = models.IntegerField()
    value = models.CharField(max_length=72)
    form_field_id = models.IntegerField(default=100)
