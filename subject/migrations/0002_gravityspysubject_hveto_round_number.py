# Generated by Django 4.0.4 on 2022-05-13 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gravityspysubject',
            name='hveto_round_number',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]
