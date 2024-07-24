from django.contrib import admin

# import models
from .models import Joke, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Joke)
