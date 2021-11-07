# Generated by Django 3.2 on 2021-10-31 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EldhrimnirApp', '0014_alter_evaluacion_materia_ponderacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia_seccion',
            name='user_edit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_edits', to=settings.AUTH_USER_MODEL),
        ),
    ]
