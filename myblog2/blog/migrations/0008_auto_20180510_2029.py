# Generated by Django 2.0 on 2018-05-10 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180510_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poetry',
            old_name='poetry',
            new_name='thepoetry',
        ),
    ]
