# Generated by Django 5.0 on 2023-12-11 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='isbn',
            field=models.CharField(max_length=13, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.CharField(blank=True, max_length=3, unique=True),
        ),
    ]
