# Generated by Django 2.1.2 on 2018-12-05 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_books_movies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
