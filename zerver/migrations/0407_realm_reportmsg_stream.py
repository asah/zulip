# Generated by Django 3.2.12 on 2022-04-09 22:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zerver", "0406_alter_realm_message_content_edit_limit_seconds"),
    ]

    operations = [
        migrations.AddField(
            model_name="realm",
            name="report_message_stream",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="zerver.stream",
            ),
        ),
    ]
