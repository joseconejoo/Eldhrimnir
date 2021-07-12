# Generated by Django 3.2 on 2021-06-22 09:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Datos1',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('nombre', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Solo letras para el nombre por favor.', regex='^[a-zA-ZñáéíóúäëïöüÑàèìòù\\s]+$')])),
                ('apellido', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Solo letras para el apellido por favor.', regex='^[a-zA-ZñáéíóúäëïöüÑàèìòù\\s]+$')])),
                ('fedicion', models.DateTimeField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('residencia', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='NivelesNum',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('coord', models.BooleanField(default=False)),
                ('ctrl_est1', models.BooleanField(default=False)),
                ('prof', models.BooleanField(default=False)),
                ('estud', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='carreras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Solo letras para el nombre por favor.', regex='^[a-zA-ZñáéíóúäëïöüÑàèìòù\\s]+$')])),
                ('date_edit', models.DateTimeField(blank=True)),
                ('user_edit', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]