from django.contrib import admin
from test_app.models import Four

# Register your models here.
class FourAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']



admin.site.register(Four,FourAdmin)