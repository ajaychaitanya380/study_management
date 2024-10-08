# Generated by Django 5.1.1 on 2024-10-08 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_name', models.CharField(max_length=100)),
                ('study_phase', models.CharField(choices=[('Phase I', 'Phase I'), ('Phase II', 'Phase II'), ('Phase III', 'Phase III'), ('Phase IV', 'Phase IV')], max_length=20)),
                ('sponsor_name', models.CharField(max_length=100)),
                ('study_description', models.TextField()),
            ],
        ),
    ]
