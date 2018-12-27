from django.contrib import admin
from .models import User
from .models import Admin
# Register your models here.

admin.site.register(User)
admin.site.register(Admin)