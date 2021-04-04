# Generated by Django 3.1.3 on 2021-03-27 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20210220_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouplesson',
            name='notes',
            field=models.CharField(choices=[('IN_PROGRESS', 1), ('COMPLETED', 2), ('NOT_STARTED', 3)], default='', max_length=300, null=True),
        ),
    ]
