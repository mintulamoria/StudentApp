# Generated by Django 2.2.17 on 2020-12-21 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0010_auto_20201221_1141'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentSectionInfo',
        ),
        migrations.AddField(
            model_name='studentclassinfo',
            name='class_short_form',
            field=models.CharField(default=11, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentclassinfo',
            name='class_name',
            field=models.IntegerField(),
        ),
    ]
