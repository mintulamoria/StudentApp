# Generated by Django 2.2.17 on 2020-12-31 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0008_auto_20201231_0956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_img',
            new_name='cover',
        ),
    ]