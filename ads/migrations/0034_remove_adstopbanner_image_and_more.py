# Generated by Django 4.1.2 on 2022-10-19 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0033_alter_ads_prize'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adstopbanner',
            name='image',
        ),
        migrations.AddField(
            model_name='adstopbanner',
            name='banner_img_url',
            field=models.CharField(blank=True, default='Place Your Banner Link', max_length=200),
        ),
    ]
