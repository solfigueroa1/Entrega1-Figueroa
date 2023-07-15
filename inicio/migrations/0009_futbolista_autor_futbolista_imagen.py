# Generated by Django 4.2.3 on 2023-07-15 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0008_alter_futbolista_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='futbolista',
            name='autor',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='futbolista',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
