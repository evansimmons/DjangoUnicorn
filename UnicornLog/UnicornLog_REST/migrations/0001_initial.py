# Generated by Django 3.2.4 on 2021-07-08 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Unicorn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('RainbowPoop', models.BooleanField(default=False)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date', models.DateField(verbose_name='%m/%d/%Y')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UnicornLog_REST.location')),
                ('unicorn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UnicornLog_REST.unicorn')),
            ],
        ),
    ]
