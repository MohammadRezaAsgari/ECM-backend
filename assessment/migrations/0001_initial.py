# Generated by Django 4.2.4 on 2023-08-22 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('product_name', models.CharField(max_length=50)),
                ('contract_number', models.CharField(max_length=50, unique=True)),
                ('date_of_contract', models.CharField(max_length=50)),
            ],
            options={
                'unique_together': {('company_name', 'product_name')},
            },
        ),
        migrations.CreateModel(
            name='ContractPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='uploads/')),
                ('contract', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='assessment.contract')),
            ],
        ),
    ]
