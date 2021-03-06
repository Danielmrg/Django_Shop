# Generated by Django 3.0.8 on 2020-07-15 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20200715_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Category'),
        ),
        migrations.AlterField(
            model_name='itemimage',
            name='image',
            field=models.ImageField(default='image/default.jpg', upload_to='image-item'),
        ),
    ]
