# Generated by Django 4.2 on 2023-04-29 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post", name="date", field=models.DateField(auto_now_add=True),
        ),
    ]