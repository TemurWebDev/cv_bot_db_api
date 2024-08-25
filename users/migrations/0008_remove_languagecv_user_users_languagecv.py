# Generated by Django 4.2.8 on 2024-05-17 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_users_languagecv_languagecv_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='languagecv',
            name='user',
        ),
        migrations.AddField(
            model_name='users',
            name='languagecv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.languagecv'),
        ),
    ]