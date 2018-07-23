from django.contrib import admin
from .models import Instrument, Bom, Instance

admin.site.register(Instrument)
admin.site.register(Bom)
admin.site.register(Instance)
