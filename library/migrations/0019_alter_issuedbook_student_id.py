# Generated by Django 5.0 on 2023-12-11 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0018_alter_issuedbook_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='student_id',
            field=models.IntegerField(blank=True),
        ),
    ]
