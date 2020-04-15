# Generated by Django 2.2.1 on 2019-06-01 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concert_name', models.CharField(max_length=200)),
                ('buy_ticket_date', models.DateTimeField(verbose_name='buy ticket time')),
                ('address', models.CharField(max_length=200)),
                ('buy_ticket_address', models.URLField(blank=True)),
                ('launch_date', models.DateTimeField(verbose_name='launch time')),
            ],
        ),
        migrations.CreateModel(
            name='Greeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('region', models.CharField(blank=True, max_length=200)),
                ('language', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket_price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('concert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Concert')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('image', models.ImageField(height_field='height', upload_to='', width_field='width')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('concert_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Concert')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='FavoriteConcert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concert_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Concert')),
            ],
        ),
        migrations.AddField(
            model_name='concert',
            name='singer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Singer'),
        ),
    ]
