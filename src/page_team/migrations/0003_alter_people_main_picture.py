# Generated by Django 4.1.1 on 2022-09-12 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_team', '0002_alter_people_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='main_picture',
            field=models.ImageField(upload_to='static/people'),
        ),
    ]
