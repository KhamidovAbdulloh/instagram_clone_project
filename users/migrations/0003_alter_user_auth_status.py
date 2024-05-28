# Generated by Django 5.0.6 on 2024-05-16 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_auth_status_user_auth_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='auth_status',
            field=models.CharField(choices=[('new', 'new'), ('code_verified', 'code_verified'), ('done', 'done'), ('photo_done', 'photo_done')], default='new', max_length=31),
        ),
    ]