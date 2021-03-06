# Generated by Django 3.2.5 on 2021-07-15 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200, null=True)),
                ('type', models.CharField(max_length=200, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('price', models.FloatField(null=True)),
                ('specs', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
