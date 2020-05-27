# Generated by Django 3.0.5 on 2020-05-27 15:11

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('crmInvisionLab', '0016_auto_20200520_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competitors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('website', models.URLField(blank=True)),
                ('position', models.CharField(blank=True, max_length=200)),
                ('contact', models.CharField(blank=True, max_length=200)),
                ('contact_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=200, region='GB')),
                ('contact_email', models.EmailField(blank=True, max_length=200)),
                ('projects', models.URLField(blank=True)),
            ],
        ),
    ]
