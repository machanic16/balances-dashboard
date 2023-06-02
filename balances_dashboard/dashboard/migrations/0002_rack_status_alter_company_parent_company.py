# Generated by Django 4.2.1 on 2023-06-02 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rack',
            name='status',
            field=models.CharField(choices=[('full', 'Full'), ('empty', 'Empty'), ('good', 'Good'), ('needs_refil', 'Needs Refil')], default='empty', max_length=30),
        ),
        migrations.AlterField(
            model_name='company',
            name='parent_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.company'),
        ),
    ]
