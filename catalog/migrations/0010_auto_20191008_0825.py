# Generated by Django 2.2.5 on 2019-10-08 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20191006_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='book',
            field=smart_selects.db_fields.ChainedManyToManyField(chained_field='language', chained_model_field='languages', horizontal=True, related_name='bookInstances', to='catalog.Book', verbose_name='book'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
