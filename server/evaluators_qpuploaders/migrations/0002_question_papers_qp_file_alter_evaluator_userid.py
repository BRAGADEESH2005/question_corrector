# Generated by Django 5.0.3 on 2024-06-22 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('evaluators_qpuploaders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question_papers',
            name='QP_File',
            field=models.FileField(default='NULL', upload_to='question_papers'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evaluator',
            name='UserID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='authentication.user'),
        ),
    ]
