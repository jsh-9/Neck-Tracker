# Generated by Django 4.0.5 on 2022-09-10 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamApp', '0003_alter_person_record_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='record_id',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
    ]