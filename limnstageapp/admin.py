from django.contrib import admin
from .models import userform, limn, limnanswer, files, asked
# Register your models here.
admin.site.register(userform)

class userModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__", 'username']
    class Meta:
        model=userform

admin.site.register(limn)
class limnModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__", 'title']
    class Meta:
        model=limn

admin.site.register(limnanswer)
class answerModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__", 'title']
    class Meta:
        model=limnanswer

admin.site.register(files)
class filesModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__", 'title']
    class Meta:
        model=files

admin.site.register(asked)
class tagsModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__", 'askeduser']
    class Meta:
        model=asked
