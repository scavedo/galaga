from django.contrib import admin
from rsi_app.models import Founders

class FoundersAdmin(admin.ModelAdmin):
    pass
admin.site.register(Founders, FoundersAdmin)
