# Generated by Django 4.0.4 on 2022-04-24 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_fk_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='fk_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.product'),
        ),
    ]
