# Generated by Django 4.2 on 2023-11-16 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_cart_sub_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartorder',
            old_name='town_city',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='cartorder',
            old_name='price',
            new_name='sub_total',
        ),
        migrations.RenameField(
            model_name='cartorderitem',
            old_name='original_grand_total',
            new_name='initial_total',
        ),
        migrations.RenameField(
            model_name='cartorderitem',
            old_name='cancel_request',
            new_name='order_placed',
        ),
        migrations.RenameField(
            model_name='cartorderitem',
            old_name='cancelled',
            new_name='processing_order',
        ),
        migrations.RenameField(
            model_name='cartorderitem',
            old_name='paid',
            new_name='product_arrived',
        ),
        migrations.RemoveField(
            model_name='cartorder',
            name='delivery_couriers',
        ),
        migrations.RemoveField(
            model_name='cartorder',
            name='delivery_status',
        ),
        migrations.RemoveField(
            model_name='cartorder',
            name='expected_delivery_date_from',
        ),
        migrations.RemoveField(
            model_name='cartorder',
            name='expected_delivery_date_to',
        ),
        migrations.RemoveField(
            model_name='cartorder',
            name='gift',
        ),
        migrations.RemoveField(
            model_name='cartorder',
            name='invoice',
        ),
        migrations.RemoveField(
            model_name='cartorder',
            name='order_placed',
        ),
        migrations.RemoveField(
            model_name='cartorder',
            name='payment_method',
        ),
        migrations.RemoveField(
            model_name='cartorder',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='cartorder',
            name='processing_order',
        ),
        migrations.RemoveField(
            model_name='cartorder',
            name='product_arrived',
        ),
        migrations.RemoveField(
            model_name='cartorder',
            name='product_delivered',
        ),
        migrations.RemoveField(
            model_name='cartorder',
            name='product_shipped',
        ),
        migrations.RemoveField(
            model_name='cartorder',
            name='quality_check',
        ),
        migrations.RemoveField(
            model_name='cartorder',
            name='success_id',
        ),
        migrations.RemoveField(
            model_name='cartorder',
            name='tracking_id',
        ),
        migrations.RemoveField(
            model_name='cartorderitem',
            name='cancel_reason',
        ),
        migrations.RemoveField(
            model_name='cartorderitem',
            name='coupon_discount_grand_total',
        ),
        migrations.RemoveField(
            model_name='cartorderitem',
            name='grand_total',
        ),
        migrations.RemoveField(
            model_name='cartorderitem',
            name='paypal_address',
        ),
        migrations.AddField(
            model_name='cartorderitem',
            name='expected_delivery_date_from',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cartorderitem',
            name='expected_delivery_date_to',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cartorderitem',
            name='product_delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cartorderitem',
            name='product_shipped',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cartorderitem',
            name='quality_check',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cartorderitem',
            name='sub_total',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Total of Product price * Product Qty', max_digits=12),
        ),
        migrations.AlterField(
            model_name='cartorder',
            name='country',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cartorderitem',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Grand Total of all amount listed above', max_digits=12),
        ),
    ]
