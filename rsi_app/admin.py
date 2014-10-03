from django.contrib import admin
from models import Founders

class FoundersAdmin(admin.ModelAdmin):
    pass
admin.site.register(Founders, FoundersAdmin)
