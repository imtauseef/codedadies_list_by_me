# Generated by Django 3.2.6 on 2021-08-15 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_field', models.CharField(max_length=200)),
                ('creation_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]