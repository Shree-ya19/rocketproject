# Generated by Django 5.1.1 on 2024-09-19 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NpjAirport', '0003_remove_csit_add'),
    ]

    operations = [
        migrations.RenameField(
            model_name='csit',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='csit',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='csit',
            old_name='Phone',
            new_name='phone',
        ),
        migrations.AlterModelTable(
            name='csit',
            table='csit',
        ),
    ]