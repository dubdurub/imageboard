from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(board)
admin.site.register(thread)
admin.site.register(Post)