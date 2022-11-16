# Generated by Django 4.1.2 on 2022-11-16 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NccsSubGroup',
            fields=[
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('label', models.CharField(default=None, max_length=256, null=True)),
            ],
            options={
                'verbose_name': 'nccs sub group',
                'verbose_name_plural': 'nccs sub groups',
                'db_table': 'non_profits_nccs_sub_group',
                'ordering': ['name'],
                'abstract': False,
            },
        ),
    ]
