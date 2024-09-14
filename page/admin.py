from django.contrib import admin
from .models import *

class KafshAdmin(admin.ModelAdmin):
    list_display=("model","price","size")
    list_max_show_all=2
    list_select_related=False
    actions=('delete','add')

admin.site.register(KafshModel,KafshAdmin)
admin.site.register(VIP)
admin.site.register(UserModel)
admin.site.register(ADModel)
