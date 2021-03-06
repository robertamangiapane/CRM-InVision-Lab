# Generated by Django 3.0.5 on 2020-05-12 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmInvisionLab', '0009_auto_20200424_0907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='collaborator',
            name='showreel',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='collaborator',
            name='ongoing_projects',
            field=models.ManyToManyField(blank=True, related_name='ongoing_projects', to='crmInvisionLab.Job'),
        ),
        migrations.AddField(
            model_name='collaborator',
            name='past_collaborations',
            field=models.ManyToManyField(blank=True, related_name='past_collaborations', to='crmInvisionLab.Job'),
        ),
    ]
