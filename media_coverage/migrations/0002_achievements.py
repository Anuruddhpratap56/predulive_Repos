# Generated by Django 4.2.2 on 2023-08-11 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_coverage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='achievements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.FileField(default=None, max_length=250, null=True, upload_to='media_coverage/')),
            ],
        ),
    ]
