"""Modulo para as classes das empresas"""
from django.db import models


class Company(models.Model):
    """Modelo da empresa"""  
    name = models.CharField(max_length=100, help_text= 'Name Company')
