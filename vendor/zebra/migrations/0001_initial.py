# Generated by Django 2.0 on 2020-06-17 07:02

import django.db.models.deletion
import zebra.mixins
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("stripe_customer_id", models.CharField(blank=True, max_length=50, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
            ],
            options={
                "abstract": False,
            },
            bases=(models.Model, zebra.mixins.StripeMixin, zebra.mixins.StripeCustomerMixin),
        ),
        migrations.CreateModel(
            name="Plan",
            fields=[
                (
                    "id",
                    models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("stripe_plan_id", models.CharField(blank=True, max_length=50, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
            ],
            options={
                "abstract": False,
            },
            bases=(models.Model, zebra.mixins.StripeMixin, zebra.mixins.StripePlanMixin),
        ),
        migrations.CreateModel(
            name="Subscription",
            fields=[
                (
                    "id",
                    models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
                (
                    "customer",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="zebra.Customer"),
                ),
                ("plan", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="zebra.Plan")),
            ],
            options={
                "abstract": False,
            },
            bases=(models.Model, zebra.mixins.StripeMixin, zebra.mixins.StripeSubscriptionMixin),
        ),
    ]
