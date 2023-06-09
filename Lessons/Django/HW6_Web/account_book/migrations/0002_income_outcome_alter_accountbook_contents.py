# Generated by Django 4.1.2 on 2022-10-18 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('contents', models.CharField(default='지출', max_length=5)),
                ('amount', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('contents', models.CharField(default='수입', max_length=5)),
                ('amount', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='accountbook',
            name='contents',
            field=models.CharField(choices=[('수입', '수입'), ('지출', '지출')], max_length=2),
        ),
    ]
