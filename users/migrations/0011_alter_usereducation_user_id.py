# Generated by Django 4.2.8 on 2024-05-24 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_skill_user_remove_usereducation_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usereducation',
            name='user_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]