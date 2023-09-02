# Generated by Django 4.2.4 on 2023-09-02 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='approved_discount',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='certificate_renewal',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='certificate_renewal_description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='contract_deadline_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='contract_total_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='first_phase_deadline_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='first_phase_deposit_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='first_phase_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='interface_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='landline_phone_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='postal_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='second_phase_deadline_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='second_phase_deposit_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='second_phase_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='supplement_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='supplement_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='SupplementFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_photo', models.ImageField(upload_to='uploads/supplement_receipt_photo/')),
                ('contract', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='assessment.contract')),
            ],
        ),
        migrations.CreateModel(
            name='PhaseTwoFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_photo', models.ImageField(upload_to='uploads/first_phase_receipt_photo/')),
                ('functional_document', models.FileField(upload_to='uploads/second_phase_functional_documents/')),
                ('vulnerability_document', models.FileField(upload_to='uploads/second_phase_vulnerability_documents/')),
                ('contract', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='assessment.contract')),
            ],
        ),
        migrations.CreateModel(
            name='PhaseOneFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_photo', models.ImageField(upload_to='uploads/first_phase_receipt_photo/')),
                ('ducuments', models.FileField(upload_to='uploads/first_phase_final_documents/')),
                ('contract', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='assessment.contract')),
            ],
        ),
    ]
