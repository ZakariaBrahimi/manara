# Generated by Django 3.2.9 on 2021-11-16 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20211116_2219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='student',
            new_name='Astudent',
        ),
        migrations.RenameField(
            model_name='assistant',
            old_name='student',
            new_name='ASSstudent',
        ),
        migrations.RenameField(
            model_name='director',
            old_name='student',
            new_name='Dstudent',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='student',
            new_name='Tstudent',
        ),
    ]
