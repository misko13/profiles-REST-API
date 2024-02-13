from django.contrib import admin

from profiles_api import models
"""we Register your models here."""

admin.site.register(models.UserProfile)

