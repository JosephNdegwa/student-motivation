# Generated by Django 4.0.3 on 2022-04-07 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motivation', '0007_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='audio_track',
            field=models.FileField(blank=True, upload_to='media/'),
        ),
    ]
