# Generated by Django 4.0a1 on 2021-10-11 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название проекта')),
                ('code', models.CharField(max_length=5, verbose_name='Код проекта')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Превью')),
                ('deadline', models.DateTimeField(blank=True, null=True, verbose_name='Дедлайн')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_projects', to='users.user', verbose_name='Автор')),
            ],
        ),
    ]
