# Generated by Django 3.2 on 2021-10-11 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EldhrimnirApp', '0010_tipo_materia'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia_seccion',
            name='tipo_mate',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='EldhrimnirApp.tipo_materia'),
            preserve_default=False,
        ),
    ]