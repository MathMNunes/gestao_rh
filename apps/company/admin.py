"""Modulo para registra no admin do django"""
from django.contrib import admin
from .models import Company


admin.site.register(Company)
