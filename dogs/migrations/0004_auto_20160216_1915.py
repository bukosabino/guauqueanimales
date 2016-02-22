# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0003_auto_20160122_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='losted',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='Nombre', blank=True),
            preserve_default=True,
        ),
    ]
