# Generated by Django 2.2.13 on 2020-06-22 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_auto_20200622_0616"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="assd",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="dfa",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="sd",
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
