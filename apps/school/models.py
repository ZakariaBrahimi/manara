from django.db import models
from django.db.models.signals import pre_delete
from apps.account.models import Director, Teacher, Student, Assistant

    

class School(models.Model):
    class SchoolStatus(models.TextChoices):
        active = 'ACTIVE', 'Active'
        unactive = 'UNACTIVE', 'UnActive'
    name        = models.CharField(max_length=200, null=True) # in the form requires a value but the database doesn't
    description = models.TextField(null=True) 
    director    = models.OneToOneField(Director, on_delete=models.PROTECT, null=True, related_name='director')
    
    # assistants  = models.ForeignKey(Assistant, on_delete=models.PROTECT, null=True, blank=True) # Optional on DB & form  #555
    
    
    teachers    = models.ManyToManyField(Teacher, related_name='teachers', blank=True) #555
    # courses     = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    status      = models.CharField(max_length=50, choices=SchoolStatus.choices, default=SchoolStatus.unactive)
    
    def totalCourses(self):
        return self.courses.count()
    
    def totalAssistants(self):
        return self.assistants.count()
    
    def totalTeachers(self):
        return self.teachers.count()
    
    def totalStudents(self):
        pass
    
    def __str__(self):
        return f'{self.name}'

class Course(models.Model):
    name = models.CharField(max_length=100)
    student = models.ManyToManyField(Student)
    school = models.OneToOneField(School, on_delete=models.PROTECT, null=True)
    def __str__(self):
        return f'{self.name}'





























def removeDirectorBadge(sender, instance, **kwargs):
    director = instance.director
    director.type = Student.Types.student
    director.save()

pre_delete.connect(receiver=removeDirectorBadge, sender=School)

def removeAssistantBadge(sender, instance, **kwargs):
    assistant = instance.assistants
    assistant.type = Student.Types.student
    assistant.save()

pre_delete.connect(receiver=removeAssistantBadge, sender=School)

def removeTeacherBadge(sender, instance, **kwargs):
    assistant = instance.teachers
    assistant.type = Student.Types.student

pre_delete.connect(receiver=removeTeacherBadge, sender=School)





    