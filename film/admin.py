from django.contrib import admin
from .models import Movies, Comments

# Register your models here.

admin.site.register(Movies)
admin.site.register(Comments)