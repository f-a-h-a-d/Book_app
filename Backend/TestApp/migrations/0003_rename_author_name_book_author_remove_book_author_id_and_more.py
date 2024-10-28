# Generated by Django 5.0.3 on 2024-04-04 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0002_book_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author_name',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author_id',
        ),
        migrations.AlterField(
            model_name='book_image',
            name='book_image',
            field=models.ImageField(blank=True, null=True, upload_to='upload_to'),
        ),
    ]