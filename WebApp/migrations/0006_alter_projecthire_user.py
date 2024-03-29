# Generated by Django 4.1.6 on 2023-02-14 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WebApp', '0005_alter_projectdeveloper_project_hire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecthire',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
