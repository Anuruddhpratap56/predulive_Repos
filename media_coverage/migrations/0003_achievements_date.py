# Generated by Django 4.2.2 on 2023-08-11 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_coverage', '0002_achievements'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievements',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
