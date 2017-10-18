# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Team(models.Model):
	team_member = models.CharField(max_length=250)
	email = models.EmailField()
	about = models.TextField()

	def __str__(self):
		return self.team_member