# Generated by Django 2.2.4 on 2019-11-18 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_details'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Details',
        ),
        migrations.AddField(
            model_name='book',
            name='user_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
