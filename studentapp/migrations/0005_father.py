# Generated by Django 2.2.17 on 2020-12-19 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0004_student_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Father',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
