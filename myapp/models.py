from __future__ import unicode_literals
from django.db import models


# class Emp(models.Model):
#     project_name = models.CharField(max_length=20)
#     startdate = models.DateTimeField()
#     enddate = models.DateTimeField()
#     valueindollars = models.IntegerField()

class Emp(models.Model):
     project_name1 = models.CharField(max_length=20, default="udit")
     startdate1 = models.DateTimeField(null=True, blank=True)
     enddate1 = models.DateTimeField(null=True, blank=True)
     valueindollars1 = models.CharField(max_length=30, default="dollar")





     class Meta:
        db_table = "Emp"

def __str__(self):
    return self.project_name1
