# Generated by Django 4.0.4 on 2022-04-23 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('review', models.CharField(blank=True, max_length=500, null=True)),
                ('stars', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('fk_product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.product')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]
