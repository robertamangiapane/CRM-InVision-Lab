# Generated by Django 3.0.5 on 2020-05-13 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmInvisionLab', '0010_auto_20200512_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='ended',
            field=models.BooleanField(default=False),
        ),
    ]