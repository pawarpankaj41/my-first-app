# Generated by Django 2.2.7 on 2019-12-20 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
        ('newuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellersprofile',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.Company'),
            preserve_default=False,
        ),
    ]