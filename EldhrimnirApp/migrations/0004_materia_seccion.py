# Generated by Django 3.2 on 2021-07-10 04:05

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EldhrimnirApp', '0003_rename_seccion_carrera_seccion_seccion_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='materia_seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia_nom', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Solo letras para el nombre por favor.', regex='^[a-zA-ZñáéíóúäëïöüÑàèìòù\\s]+$')])),
                ('date_edit', models.DateTimeField(blank=True)),
                ('profesor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profesors', to=settings.AUTH_USER_MODEL)),
                ('seccion', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='EldhrimnirApp.carrera_seccion')),
                ('user_edit', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_edits', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
