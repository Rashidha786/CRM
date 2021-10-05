from django.db import models
from django.contrib.auth.models import User


class Emp_Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=25, blank=True, null=True)
    team_name = models.CharField(max_length=25, blank=True, null=True)
    team_lead = models.CharField(max_length=25, blank=True, null=True)
    designation = models.CharField(max_length=25, blank=True, null=True)


