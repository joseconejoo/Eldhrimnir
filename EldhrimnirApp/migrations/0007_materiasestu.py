# Generated by Django 3.2 on 2021-09-13 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EldhrimnirApp', '0006_alter_datos1_residencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='MateriasEstu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EldhrimnirApp.materia_seccion')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
