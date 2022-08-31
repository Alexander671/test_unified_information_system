# Generated by Django 4.1 on 2022-08-31 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accrual', '0002_alter_accrual_month_alter_payment_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accrual',
            name='month',
            field=models.PositiveSmallIntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'Decemberry')], null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='month',
            field=models.PositiveSmallIntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'Decemberry')], null=True),
        ),
    ]