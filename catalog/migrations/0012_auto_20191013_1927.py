# Generated by Django 2.2.5 on 2019-10-13 19:27

import catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20191013_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='due_back_date',
            field=models.DateField(blank=True, null=True, validators=[catalog.models.BookInstance.validate_date]),
        ),
    ]
