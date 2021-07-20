# Generated by Django 3.2.5 on 2021-07-15 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nanoitems', '0002_promotion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='promotion',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nanoitems.product'),
        ),
        migrations.AddField(
            model_name='promotion',
            name='tags',
            field=models.ManyToManyField(to='nanoitems.Tag'),
        ),
    ]
