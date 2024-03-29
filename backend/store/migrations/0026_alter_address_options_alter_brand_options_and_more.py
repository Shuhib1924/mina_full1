# Generated by Django 5.0.1 on 2024-03-07 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_alter_product_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Adressen'},
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name_plural': 'Marken'},
        ),
        migrations.AlterModelOptions(
            name='cancelledorder',
            options={'verbose_name_plural': 'Abgebrochene Bestellungen'},
        ),
        migrations.AlterModelOptions(
            name='cartorder',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Bestellungen'},
        ),
        migrations.AlterModelOptions(
            name='cartorderitem',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Warenkorb Element'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Kategorien'},
        ),
        migrations.AlterModelOptions(
            name='deliverycouriers',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Fahrer'},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'ordering': ['date'], 'verbose_name_plural': 'Gallerie'},
        ),
        migrations.AlterModelOptions(
            name='notification',
            options={'verbose_name_plural': 'Meldung'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Produkte'},
        ),
        migrations.AlterModelOptions(
            name='productfaq',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Produkt Fragen'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Rezension'},
        ),
        migrations.AlterModelOptions(
            name='wishlist',
            options={'verbose_name_plural': 'Wunschliste'},
        ),
        migrations.AlterField(
            model_name='cartorder',
            name='order_status',
            field=models.CharField(choices=[('Pending', 'wartend'), ('Fulfilled', 'erledigt'), ('Partially Fulfilled', 'teilweise erledigt'), ('Cancelled', 'abgebrochen')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='cartorder',
            name='payment_status',
            field=models.CharField(choices=[('paid', 'bezahlt'), ('pending', 'wartend'), ('processing', 'Prozess'), ('cancelled', 'abgebrochen'), ('initiated', 'initialisiert'), ('failed', 'fehler'), ('refunding', 'wird erstattet'), ('refunded', 'wurde erstatted'), ('unpaid', 'nicht bezahlt'), ('expired', 'abgelaufen')], default='initiated', max_length=100),
        ),
        migrations.AlterField(
            model_name='cartorderitem',
            name='delivery_status',
            field=models.CharField(choices=[('On Hold', 'wartend'), ('Shipping Processing', 'Prozess'), ('Shipped', 'versendet'), ('Arrived', 'erreicht'), ('Delivered', 'geliefert'), ('Returning', 'wird erstattet'), ('Returned', 'Rückerstattet')], default='On Hold', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(blank=True, choices=[('draft', 'vorlage'), ('disabled', 'unmöglich'), ('rejected', 'abgelehnt'), ('in_review', 'vorschau'), ('published', 'veröffentlicht')], default='published', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('regular', 'regulär'), ('auction', 'Auktion'), ('offer', 'angebot')], default='regular', max_length=50),
        ),
    ]
