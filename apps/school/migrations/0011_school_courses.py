# Generated by Django 3.2.9 on 2021-11-17 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='courses',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.course'),
        ),
    ]
