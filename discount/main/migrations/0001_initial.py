# Generated by Django 4.1.6 on 2023-02-13 15:41

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
                ('expire_date', models.DateField(default=datetime.datetime(2024, 2, 13, 15, 41, 15, 827021, tzinfo=datetime.timezone.utc))),
                ('last_used_date', models.DateTimeField()),
                ('total', models.PositiveIntegerField(default=0)),
                ('main', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='CardSeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=6, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'seria',
                'verbose_name_plural': 'seria',
            },
        ),
        migrations.CreateModel(
            name='CardStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'status',
                'verbose_name_plural': 'statuses',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.card')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('main', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.DecimalField(decimal_places=2, max_digits=5)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.product')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='seria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cardseria'),
        ),
        migrations.AddField(
            model_name='card',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cardstatus'),
        ),
    ]
