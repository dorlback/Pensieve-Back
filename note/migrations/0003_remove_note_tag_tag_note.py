# Generated by Django 5.0.6 on 2024-06-20 09:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("note", "0002_rename_field_name_note_content_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="note",
            name="tag",
        ),
        migrations.AddField(
            model_name="tag",
            name="note",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="note_id",
                to="note.note",
            ),
            preserve_default=False,
        ),
    ]
