# Generated by Django 3.2.7 on 2021-10-05 18:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0008_alter_bonafide_date_of_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonafide',
            name='date_of_request',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]