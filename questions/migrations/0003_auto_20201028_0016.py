# Generated by Django 3.1.2 on 2020-10-27 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20201028_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject_db',
            name='subject_code',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
