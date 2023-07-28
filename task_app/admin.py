from django.contrib import admin
from . import models
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
  list_display = ("task", "description", "due_date",)

admin.site.register(models.Task,TaskAdmin)
# admin.site.register(models.user_view)
