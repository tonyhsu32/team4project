# Generated by Django 2.1.1 on 2018-09-19 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productid', models.AutoField(primary_key=True, serialize=False)),
                ('modelnumber', models.CharField(max_length=45)),
                ('modelname', models.CharField(max_length=45)),
                ('productimage', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=300)),
                ('categoryid', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
