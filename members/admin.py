from django.contrib import admin
from .models import *


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id','group_name']

@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display = ['id','group','club','club_members','flag']

@admin.register(CsvFile)
class CsvFileAdmin(admin.ModelAdmin):
    list_display = ['id','csv_file']
