# Generated by Django 4.1.2 on 2022-11-28 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareportsystem', '0003_remove_student_nationality_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='Month',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], default='1'),
        ),
    ]
