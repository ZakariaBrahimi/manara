from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# from apps.school.models import School

class StudentManager(BaseUserManager):
    def create_user(self, *args, **kwargs):
        pass
    def create_superuser(self, *args, **kwargs):
        
        return super().create_superuser(*args, **kwargs)

class Student(AbstractUser):
    third_name = models.CharField(max_length=100)
    email      = models.EmailField(blank=False, null=False, unique=True)
    class Types(models.TextChoices):
        student = 'STUDENT', 'Student'
        teacher = 'TEACHER', 'Teacher'
        assistant = 'ASSISTANT', 'Assistant'
        director = 'DIRECTOR', 'Director'
        admin = 'ADMIN', 'Admin'
        
    type = models.CharField(max_length=50, choices=Types.choices, default=Types.student)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username',]
    USERNAME_FIELD = 'email'
    def __str__(self):
        return f'{self.username}'
    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.type = Student.Types.admin
        return super().save(*args, **kwargs)
Student._meta.get_field('first_name').blank = False
Student._meta.get_field('first_name').null = False
Student._meta.get_field('last_name').blank = False
Student._meta.get_field('last_name').null = False



class AdminManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Student.Types.admin)

class DirectorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Student.Types.director)

class AssistantManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Student.Types.assistant)

class TeacherManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Student.Types.teacher)


class Admin(Student):
    #TODO: https://docs.djangoproject.com/en/3.2/topics/db/models/
    objects = AdminManager()
    class Meta:
        proxy = True
    def save(self, *args, **kwargs):
        self.is_superuser = True
        self.is_staff = True
        if not self.pk:
            self.type = Student.Types.admin
        return super().save(*args, **kwargs)

class Director(Student):
    objects = DirectorManager()
    class Meta:
        proxy = True
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = Student.Types.director
        return super().save(*args, **kwargs)

class Assistant(Student):
    objects = AssistantManager()
    class Meta:
        proxy = True
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = Student.Types.assistant
        return super().save(*args, **kwargs)

class Teacher(Student):
    objects = TeacherManager()
    class Meta:
        proxy = True
    def save(self, *args, **kwargs):
        #TODO
        # save it as a note
        # How we detect a new instance of the model created or not !!
        if not self.pk:
            self.type = Student.Types.teacher
        return super().save(*args, **kwargs)
    
    
class AdminModel(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, db_constraint=False)

class DirectorModel(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, db_constraint=False)
    
class AssistantModel(models.Model):
    shcools  = models.ForeignKey('school.School', on_delete=models.PROTECT,related_name='school', null=True, blank=True) # Optional on DB & form  #555
    student = models.OneToOneField(Student, on_delete=models.CASCADE, db_constraint=False)
class TeacherModel(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, db_constraint=False)


