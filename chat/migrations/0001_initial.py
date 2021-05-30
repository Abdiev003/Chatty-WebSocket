# Generated by Django 3.2.3 on 2021-05-30 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('room', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('data_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('data_added',),
            },
        ),
    ]
