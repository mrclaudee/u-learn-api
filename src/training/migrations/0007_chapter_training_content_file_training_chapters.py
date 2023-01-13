# Generated by Django 4.1.2 on 2022-12-19 13:48

from django.db import migrations, models
import training.models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0006_training_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='training',
            name='content_file',
            field=models.FileField(blank=True, default='training/default.pdf', upload_to=training.models.upload_to),
        ),
        migrations.AddField(
            model_name='training',
            name='chapters',
            field=models.ManyToManyField(blank=True, related_name='chapters', to='training.chapter'),
        ),
    ]
