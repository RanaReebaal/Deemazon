# Generated by Django 4.1.3 on 2022-11-11 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jewelleryhouse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jewelleryhouse',
            old_name='jewelleryhouse_brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='jewelleryhouse',
            old_name='jewelleryhouse_images',
            new_name='images',
        ),
        migrations.RenameField(
            model_name='jewelleryhouse',
            old_name='jewelleryhouse_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='jewelleryhouse',
            old_name='jewelleryhouse_quailty',
            new_name='quailty',
        ),
    ]
