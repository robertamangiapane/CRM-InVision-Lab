# Generated by Django 3.0.5 on 2020-04-17 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmInvisionLab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborator',
            name='availability',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='collaborator',
            name='position',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]