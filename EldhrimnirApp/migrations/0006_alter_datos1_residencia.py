# Generated by Django 3.2 on 2021-08-16 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EldhrimnirApp', '0005_nivelesnum2_nivelusu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos1',
            name='residencia',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
