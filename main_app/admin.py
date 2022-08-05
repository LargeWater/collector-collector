from django.contrib import admin

# Register your models here.
from .models import Collector, Website, Follower

admin.site.register(Collector)
admin.site.register(Website)
admin.site.register(Follower)