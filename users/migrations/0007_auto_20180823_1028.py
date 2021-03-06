# Generated by Django 2.0.7 on 2018-08-23 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_usersroles'),
    ]

    operations = [
        migrations.CreateModel(
            name='RolesPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='group',
            name='permissions',
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='usersroles',
            name='group',
            field=models.ForeignKey(db_column='CG_UM_ROLE_ID', on_delete=django.db.models.deletion.CASCADE, to='users.Group'),
        ),
        migrations.AlterField(
            model_name='usersroles',
            name='user',
            field=models.ForeignKey(db_column='CG_UM_ALTER_EMPLID', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rolespermissions',
            name='group',
            field=models.ForeignKey(db_column='CG_ROLE_ID', on_delete=django.db.models.deletion.CASCADE, to='users.Group'),
        ),
        migrations.AddField(
            model_name='rolespermissions',
            name='permissions',
            field=models.ForeignKey(db_column='CG_PERMISSION_ID', on_delete=django.db.models.deletion.CASCADE, to='users.Permissions'),
        ),
    ]
