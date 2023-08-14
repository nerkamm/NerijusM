from django.contrib import admin

# Register your models here.
from .models import Budas, Lapas, LapasInstance, Vadovas, Profilis


class LapasInstanceAdmin(admin.ModelAdmin):
    list_display = ('lapas', 'status', 'issued', 'due_valid', 'reader')
    list_filter = ('status', 'due_valid')


admin.site.register(Budas)
admin.site.register(Lapas)
admin.site.register(LapasInstance, LapasInstanceAdmin)
admin.site.register(Vadovas)
admin.site.register(Profilis)
