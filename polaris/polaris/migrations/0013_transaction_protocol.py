# Generated by Django 2.2.12 on 2020-04-23 20:21

from django.db import migrations, models
from polaris.models import Transaction


def default_sep24(apps, schema_editor):
    """
    Any existing transactions prior to this migration are SEP-24 transactions
    """
    Transaction.objects.update(protocol=Transaction.PROTOCOL.sep24)


class Migration(migrations.Migration):

    dependencies = [
        ("polaris", "0012_auto_20200420_2205"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="protocol",
            field=models.CharField(
                choices=[("sep6", "sep6"), ("sep24", "sep24")], null=True, max_length=5
            ),
        ),
        migrations.RunPython(default_sep24),
    ]
