from django.contrib import admin
from apps.account.models import Student, Teacher, Director, AssistantModel, Admin

class StudentList(admin.ModelAdmin):
    list_display = ('email', 'username','id', 'is_active', 'type' )
class DirectorList(admin.ModelAdmin):
    list_display = ('username', 'id','type', )

admin.site.register(Student, StudentList)
admin.site.register(Director, DirectorList)
admin.site.register(Teacher)
admin.site.register(AssistantModel)
admin.site.register(Admin)
