from django.contrib import admin

# Register your models here.
from .models import Actual,Sport,Newest,News,Show,Tech,Lifestyle,Viral

admin.site.register(Actual)
admin.site.register(Sport)
admin.site.register(Newest)
admin.site.register(News)
admin.site.register(Show)
admin.site.register(Tech)
admin.site.register(Lifestyle)
admin.site.register(Viral)