# Generated by Django 4.1.2 on 2023-01-17 17:39

from django.db import migrations, models
import training.models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0007_chapter_training_content_file_training_chapters'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='file_url',
            field=models.FileField(blank=True, default='training/default.pdf', upload_to=training.models.upload_to),
        ),
    ]
