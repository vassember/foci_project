from app.models import Meccs,Csapat,Eredmeny
from django.contrib import admin

#class AdminMod(admin.ModelAdmin):

	
admin.site.register(Meccs)
admin.site.register(Csapat)
admin.site.register(Eredmeny)
