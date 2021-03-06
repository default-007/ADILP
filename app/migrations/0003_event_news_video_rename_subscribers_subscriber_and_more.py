# Generated by Django 4.0.3 on 2022-03-02 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_subscribers_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='News_video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_link', models.URLField(max_length=300, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Subscribers',
            new_name='Subscriber',
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.event')),
            ],
        ),
    ]
