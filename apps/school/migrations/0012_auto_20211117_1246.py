# Generated by Django 3.2.9 on 2021-11-17 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_school_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='courses',
        ),
        migrations.AddField(
            model_name='course',
            name='school',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='school.school'),
        ),
    ]