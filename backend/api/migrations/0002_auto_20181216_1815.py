# Generated by Django 2.1.3 on 2018-12-16 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='workout',
        ),
        migrations.AddField(
            model_name='exercise',
            name='workout',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.Workout'),
        ),
    ]
