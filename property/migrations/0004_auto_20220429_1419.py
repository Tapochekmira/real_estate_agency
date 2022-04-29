# Generated by Django 3.2.12 on 2022-04-29 11:19

from django.db import migrations


def fill_newbuilding_field(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.new_building = flat.construction_year >= 2015
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(fill_newbuilding_field)
    ]