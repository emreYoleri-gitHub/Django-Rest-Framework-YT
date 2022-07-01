# Generated by Django 4.0.5 on 2022-07-01 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('athor', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('release_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('date_of_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
