# Generated by Django 4.0.6 on 2022-07-04 15:45

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.DecimalField(decimal_places=2, default='0.00', max_digits=10)),
                ('image', models.URLField()),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField(default=None)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
            ],
        ),
    ]
