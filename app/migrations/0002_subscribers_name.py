# Generated by Django 4.0.3 on 2022-03-02 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribers',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
