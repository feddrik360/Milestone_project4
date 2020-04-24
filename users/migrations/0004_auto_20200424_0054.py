# Generated by Django 2.2 on 2020-04-23 23:54

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200424_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, default='default.jpg', force_format=None, keep_meta=True, quality=0, size=[500, 300], upload_to='profile_pics'),
        ),
    ]