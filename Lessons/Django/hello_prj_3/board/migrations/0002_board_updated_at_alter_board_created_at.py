# Generated by Django 4.0.3 on 2022-10-14 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]