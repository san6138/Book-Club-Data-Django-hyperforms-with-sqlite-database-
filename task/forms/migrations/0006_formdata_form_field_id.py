# Generated by Django 4.1.1 on 2023-07-30 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_rename_record_formdata_record_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdata',
            name='form_field_id',
            field=models.IntegerField(default=None),
        ),
    ]
