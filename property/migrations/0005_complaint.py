# Generated by Django 2.2.24 on 2023-05-16 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0004_auto_20230516_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.TextField(verbose_name='Текст жалобы')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adress_complaints', to='property.Flat', verbose_name='Квартира, на которую пожаловались')),
                ('complainterator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_complaints', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался')),
            ],
        ),
    ]