# Generated by Django 2.0 on 2018-08-20 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='emp_id',
            field=models.CharField(blank=True, db_column='CG_UM_ALTER_EMPLID', max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, db_column='CG_UM_FIRST_NAME', max_length=255, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, db_column='CG_UM_LAST_NAME', max_length=255, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='user',
            name='middle_name',
            field=models.CharField(blank=True, db_column='CG_UM_MIDDLE_NAME', max_length=255, verbose_name='middle name'),
        ),
        migrations.AddField(
            model_name='user',
            name='pref_first_name',
            field=models.CharField(blank=True, db_column='CG_UM_PREF_FIRST_NAME', max_length=255, verbose_name='preferred first name'),
        ),
        migrations.AddField(
            model_name='user',
            name='pref_language',
            field=models.CharField(blank=True, db_column='CG_UM_PREF_LANG', max_length=3, verbose_name='preferred language'),
        ),
        migrations.AddField(
            model_name='user',
            name='pref_last_name',
            field=models.CharField(blank=True, db_column='CG_UM_PREF_LAST_NAME', max_length=255, verbose_name='preferred last name'),
        ),
        migrations.AddField(
            model_name='user',
            name='title',
            field=models.CharField(blank=True, choices=[('Mr.', 'Mr'), ('Mrs.', 'Mrs'), ('Ms.', 'Ms')], db_column='CG_UM_TITLE', max_length=5, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='user',
            name='active',
            field=models.BooleanField(db_column='CG_UM_STATUS', default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_column='CG_UM_EMAIL', max_length=255, unique=True, verbose_name='email address'),
        ),
    ]
