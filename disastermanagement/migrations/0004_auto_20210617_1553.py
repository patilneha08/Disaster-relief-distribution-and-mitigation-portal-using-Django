# Generated by Django 3.2.3 on 2021-06-17 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disastermanagement', '0003_rename_services_service'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='service1',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='service2',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='service3',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='service4',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='service5',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='service6',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='service7',
            field=models.CharField(default='', max_length=64),
        ),
    ]
