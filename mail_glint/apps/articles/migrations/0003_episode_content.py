# Generated by Django 3.2.16 on 2024-06-05 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='에피소드 내용'),
        ),
    ]