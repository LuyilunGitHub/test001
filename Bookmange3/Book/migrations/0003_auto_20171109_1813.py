# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0002_areainfo_pictureinfo'),
    ]

    operations = [
       
        migrations.AlterField(
            model_name='pictureinfo',
            name='path',
            field=models.ImageField(upload_to='Book/'),
        ),
    ]
