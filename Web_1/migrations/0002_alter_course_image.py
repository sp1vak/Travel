# Generated by Django 4.2.5 on 2024-06-05 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(null=True, upload_to='course_images', verbose_name='Картинка'),
        ),
    ]