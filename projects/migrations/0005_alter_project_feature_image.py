# Generated by Django 4.1.1 on 2022-11-02 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_feature_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='feature_image',
            field=models.ImageField(blank=True, default='default.jpeg', null=True, upload_to=''),
        ),
    ]
