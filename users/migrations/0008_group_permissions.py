# Generated by Django 2.0.7 on 2018-08-23 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20180823_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='permissions',
            field=models.ManyToManyField(blank=True, through='users.RolesPermissions', to='users.Permissions'),
        ),
    ]
