# Generated by Django 3.1 on 2021-11-20 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0011_auto_20211120_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parentComment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contest.comment'),
        ),
    ]