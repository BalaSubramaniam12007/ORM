# Generated by Django 5.1.3 on 2024-11-17 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bankloan',
            fields=[
                ('loan_id', models.IntegerField(primary_key=True, serialize=False)),
                ('loan_type', models.CharField(max_length=100)),
                ('loan_amt', models.IntegerField()),
                ('cust_no', models.IntegerField()),
                ('cust_name', models.CharField(max_length=100)),
            ],
        ),
    ]
