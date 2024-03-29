# Generated by Django 4.2.1 on 2023-06-02 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent_company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.company')),
            ],
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.company')),
            ],
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_weight', models.FloatField()),
                ('min_weight', models.FloatField()),
                ('rack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.rack')),
            ],
        ),
        migrations.AddField(
            model_name='rack',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.store'),
        ),
    ]
