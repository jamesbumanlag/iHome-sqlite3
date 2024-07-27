from django.contrib import admin
from .models import Record, PersonalCare, MobilityAssistance,NutritionHydration,HealthMonitoring, Activities, Housekeeping, ProgressNotes

admin.site.register(Record)
admin.site.register(PersonalCare)
admin.site.register(MobilityAssistance)
admin.site.register(NutritionHydration)
admin.site.register(HealthMonitoring)
admin.site.register(Activities)
admin.site.register(Housekeeping)
admin.site.register(ProgressNotes)