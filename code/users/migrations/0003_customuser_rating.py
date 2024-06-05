# Generated by Django 5.0.6 on 2024-05-17 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3, verbose_name='Рейтинг'),
        ),
    ]