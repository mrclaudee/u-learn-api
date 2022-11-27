# Generated by Django 4.1.2 on 2022-11-27 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('registered', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('coming', 'Coming'), ('available', 'Available')], default='coming', max_length=9)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='training.category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('training', models.ManyToManyField(to='training.training')),
            ],
        ),
    ]
