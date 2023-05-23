# Generated by Django 2.2.24 on 2023-05-18 13:17

from django.db import migrations


class Migration(migrations.Migration):
    def migrate_flats_owners_to_owner(apps, schema_editor):
        Flat = apps.get_model('property', 'Flat')
        Owner = apps.get_model('property', 'Owner')

        for flat in Flat.objects.all():
            Owner.objects.get_or_create(
                owner=flat.owner,
                owners_phonenumber=flat.owners_phonenumber,
                owner_pure_phone=flat.owner_pure_phone,
            )
        for owner in Owner.objects.all():
            owner.flats.add(*Flat.objects.filter(owner=owner.owner))

    def migrate_backward(apps, schema_editor):
        Owner = apps.get_model('property', 'Owner')
        for owner in Owner.objects.all():
            owner.update_or_create(
                owner=None,
                owners_phonenumber=None,
                owner_pure_phone=None,
                flats=None
            )

    dependencies = [
        ('property', '0005_owner'),
    ]

    operations = [
        migrations.RunPython(
            migrate_flats_owners_to_owner,
            migrate_backward
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
    ]