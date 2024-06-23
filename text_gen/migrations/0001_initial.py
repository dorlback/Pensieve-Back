# Generated by Django 5.0.6 on 2024-06-05 17:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ChatSession",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("session", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("created_date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "chat_session",
            },
        ),
    ]