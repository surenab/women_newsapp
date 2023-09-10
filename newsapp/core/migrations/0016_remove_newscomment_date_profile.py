# Generated by Django 4.2.4 on 2023-09-08 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0015_message_date_news_view_count_newscomment_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newscomment',
            name='date',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='asets/img/albert.jpg', upload_to='images')),
                ('tel', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('birthday', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
