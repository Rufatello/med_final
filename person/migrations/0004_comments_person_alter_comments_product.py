# Generated by Django 5.0.3 on 2024-03-18 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_product', to='person.person', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_product', to='person.product', verbose_name='Продукт'),
        ),
    ]
