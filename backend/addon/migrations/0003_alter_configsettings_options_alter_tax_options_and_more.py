# Generated by Django 5.0.1 on 2024-03-07 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addon', '0002_rename_settings_configsettings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='configsettings',
            options={'verbose_name': 'Einstellung', 'verbose_name_plural': 'Einstellungen'},
        ),
        migrations.AlterModelOptions(
            name='tax',
            options={'verbose_name_plural': 'Steuersatz'},
        ),
        migrations.AlterField(
            model_name='configsettings',
            name='currency_abbreviation',
            field=models.CharField(default='EUR', max_length=10),
        ),
        migrations.AlterField(
            model_name='configsettings',
            name='currency_sign',
            field=models.CharField(default='€', max_length=10),
        ),
        migrations.AlterField(
            model_name='configsettings',
            name='service_fee_charge_type',
            field=models.CharField(choices=[('percentage', 'Prozentual'), ('flat_rate', 'Pauschalbetrag')], default='percentage', max_length=30),
        ),
        migrations.AlterField(
            model_name='configsettings',
            name='view_more',
            field=models.CharField(default='Alle Anzeigen', max_length=10),
        ),
    ]
