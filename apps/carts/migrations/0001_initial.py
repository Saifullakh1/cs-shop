# Generated by Django 5.0.1 on 2024-02-27 07:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clothes', '0004_clothes_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothes_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_clothes', to='clothes.clothes', verbose_name='Одежда')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_users', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
    ]