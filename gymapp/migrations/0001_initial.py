# Generated by Django 5.0.2 on 2024-02-15 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('PhoneNumber', models.BigIntegerField()),
            ],
        ),
    ]
