# Generated by Django 4.1.2 on 2022-12-06 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareportsystem', '0008_alter_report_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='Month',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], default='1', max_length=3),
        ),
    ]
