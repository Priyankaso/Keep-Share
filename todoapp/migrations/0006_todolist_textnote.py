# Generated by Django 2.0 on 2020-06-10 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_auto_20200509_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='textnote',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]