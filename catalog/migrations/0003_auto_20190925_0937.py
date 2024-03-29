# Generated by Django 2.2.5 on 2019-09-25 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20190924_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(null=True),
        ),
        migrations.RemoveField(
            model_name='book',
            name='languages',
        ),
        migrations.AddField(
            model_name='book',
            name='languages',
            field=models.ManyToManyField(through='catalog.BookLanguage',
                                         to='catalog.Language'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='borrower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='due_back_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.BookLanguage'),
        ),
        migrations.AddField(
            model_name='booklanguage',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Book'),
        ),
        migrations.AddField(
            model_name='booklanguage',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Language'),
        ),
    ]
