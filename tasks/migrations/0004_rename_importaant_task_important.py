# Generated by Django 4.1 on 2023-02-27 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_datecompleted_alter_task_descrition'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='importaant',
            new_name='important',
        ),
    ]