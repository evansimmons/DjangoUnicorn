# Generated by Django 3.2.4 on 2021-07-14 03:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UnicornLog_REST', '0003_auto_20210713_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='sighting',
            name='witness',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
