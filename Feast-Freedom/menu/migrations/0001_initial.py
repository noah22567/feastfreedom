# Generated by Django 2.2.2 on 2019-06-19 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('provider', '0007_auto_20190619_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
                ('is_veg', models.BooleanField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('kitchen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.Kitchen')),
            ],
        ),
    ]
