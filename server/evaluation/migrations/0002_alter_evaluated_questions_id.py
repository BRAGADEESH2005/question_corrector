# Generated by Django 5.0.6 on 2024-05-29 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluated_questions',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]