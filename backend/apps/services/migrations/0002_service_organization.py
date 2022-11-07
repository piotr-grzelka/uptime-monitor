# Generated by Django 4.1.2 on 2022-11-07 18:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organizations", "0003_alter_organizationuser_organization"),
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="organization",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="organizations.organization",
                verbose_name="Organization",
            ),
            preserve_default=False,
        ),
    ]