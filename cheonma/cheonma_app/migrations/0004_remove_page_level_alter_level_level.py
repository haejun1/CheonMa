# Generated by Django 4.2.9 on 2024-01-22 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cheonma_app', '0003_level_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='level',
        ),
        migrations.AlterField(
            model_name='level',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cheonma_app.page'),
        ),
    ]
