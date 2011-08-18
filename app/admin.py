from app.models import Meccs,Csapat
from django.contrib import admin

#class AdminMod(admin.ModelAdmin):
#		list_display=('name','date')
	
admin.site.register(Meccs)
admin.site.register(Csapat)

