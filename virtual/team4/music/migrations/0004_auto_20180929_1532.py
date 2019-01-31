# Generated by Django 2.1.1 on 2018-09-29 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20180926_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderhistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateTimeField()),
                ('order_num', models.IntegerField()),
                ('this_song_order_num', models.IntegerField()),
            ],
            options={
                'db_table': 'orderhistory',
            },
        ),
        migrations.AlterModelOptions(
            name='member',
            options={},
        ),
        migrations.AlterModelOptions(
            name='songlist',
            options={},
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='music.Member'),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='music.Songlist'),
        ),
    ]
