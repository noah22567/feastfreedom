# Generated by Django 2.2.2 on 2019-06-16 22:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServiceProviderName', models.CharField(max_length=20, verbose_name='Service provider name')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Starttime', models.TimeField(verbose_name='Start Time')),
                ('Endtime', models.TimeField(verbose_name='End Time')),
                ('Kitchenimg', models.ImageField(blank=True, upload_to='images/')),
                ('ServiceProviderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.ServiceProvider')),
            ],
        ),
    ]