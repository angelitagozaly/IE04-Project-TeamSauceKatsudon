# Generated by Django 4.1.2 on 2022-12-06 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tareportsystem', '0012_alter_course_courseid_alter_course_coursename_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporthour',
            name='ReportTitle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tareportsystem.report', verbose_name='Report Title'),
        ),
    ]
