# Generated by Django 5.0.4 on 2024-04-11 12:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students_mentors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubscriptionID', models.CharField(max_length=10)),
                ('SubscriptionStartDate', models.DateField()),
                ('SubscriptionEndDate', models.DateField()),
                ('isOver', models.BooleanField()),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students_mentors.student')),
            ],
        ),
    ]
