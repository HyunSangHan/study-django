# Generated by Django 2.1.7 on 2019-05-14 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='feed_photos'),
        ),
    ]