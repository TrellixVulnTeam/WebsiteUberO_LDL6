# Generated by Django 2.2.6 on 2019-11-05 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_auto_20191105_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationform',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
