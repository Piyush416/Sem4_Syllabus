# Generated by Django 5.0.3 on 2024-03-16 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_rename_contact_contact_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_data',
            name='desc',
            field=models.TextField(),
        ),
    ]
