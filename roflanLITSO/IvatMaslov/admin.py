from django.contrib import admin
from .models import Person
from .models import rap
from .models import info
from .models import look
from .models import famous


# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname')
class rapAdmin(admin.ModelAdmin):
    list_display = ('type','borncounrty')
class infoAdmin(admin.ModelAdmin):
    list_display = ('opred','history')
class lookAdmin(admin.ModelAdmin):
    list_display = ('types',)
class famousAdmin(admin.ModelAdmin):
    list_display = ('Person','squade')

admin.site.register(Person, PersonAdmin)
admin.site.register(rap, rapAdmin)
admin.site.register(info, infoAdmin)
admin.site.register(look, lookAdmin)
admin.site.register(famous, famousAdmin)