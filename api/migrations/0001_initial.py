# Generated by Django 4.2.2 on 2023-06-13 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NextEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(default='', max_length=100)),
                ('event_bio', models.TextField()),
                ('event_ends_on', models.DateTimeField()),
                ('event_img', models.ImageField(upload_to='imgs/events')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('deadline', models.DateTimeField()),
            ],
        ),
    ]
