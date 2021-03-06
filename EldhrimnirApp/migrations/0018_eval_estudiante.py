# Generated by Django 3.2 on 2021-11-08 03:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EldhrimnirApp', '0017_alter_evaluacion_materia_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='eval_estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.PositiveIntegerField()),
                ('asistente', models.BooleanField(default=False)),
                ('evaluacion_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EldhrimnirApp.evaluacion_materia')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
