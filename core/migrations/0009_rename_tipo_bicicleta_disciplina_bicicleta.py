# Generated by Django 3.2.3 on 2021-05-27 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210527_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disciplina',
            old_name='tipo_bicicleta',
            new_name='bicicleta',
        ),
    ]