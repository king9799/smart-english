from django.contrib import admin
from .models import Student, Timetable

class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student, StudentAdmin)


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = [
        'subject_name', 'lesson_pattern', 'lesson_type', 
        'group_type', 'start_time', 'finish_time'
                   ]
