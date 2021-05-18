from django.contrib import admin
from .models import Student, Timetable, Profile, Building

class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student, StudentAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = [
        'subject_name', 'lesson_pattern', 'lesson_type', 
        'group_type', 'start_time', 'finish_time'
                   ]

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
	list_display = ['name', 'location', 'room_amount', 'nickname', 'added_time']
	