from django.contrib import admin

# Register your models here.
from computers.models import Computer, OS, Producer

admin.site.register(Computer)
admin.site.register(OS)
admin.site.register(Producer)