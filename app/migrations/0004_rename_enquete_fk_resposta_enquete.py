# Generated by Django 3.2.9 on 2021-11-28 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_resposta_enquete_fk'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resposta',
            old_name='enquete_fk',
            new_name='enquete',
        ),
    ]