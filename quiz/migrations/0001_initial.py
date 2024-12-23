# Generated by Django 4.2.5 on 2024-12-22 21:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Question",
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
                (
                    "topic",
                    models.CharField(
                        choices=[
                            ("os", "Operating Systems"),
                            ("dbms", "Database Management Systems"),
                            ("dsa", "Data Structures & Algorithms"),
                            ("networks", "Networks"),
                            ("cloud", "Cloud Computing"),
                            ("web", "Web Development"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "difficulty",
                    models.CharField(
                        choices=[
                            ("beginner", "Beginner"),
                            ("intermediate", "Intermediate"),
                            ("advanced", "Advanced"),
                        ],
                        max_length=20,
                    ),
                ),
                ("question_text", models.TextField()),
                ("correct_answer", models.CharField(max_length=255)),
                ("option_1", models.CharField(blank=True, max_length=255)),
                ("option_2", models.CharField(blank=True, max_length=255)),
                ("option_3", models.CharField(blank=True, max_length=255)),
                ("option_4", models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="UserResult",
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
                ("topic", models.CharField(max_length=100)),
                ("score", models.IntegerField()),
                ("total_questions", models.IntegerField(default=8)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
