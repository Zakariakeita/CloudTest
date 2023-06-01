# Generated by Django 4.2.1 on 2023-06-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Participant",
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
                ("nom", models.CharField(max_length=70)),
                ("prenom", models.CharField(max_length=70)),
                ("numero", models.CharField(max_length=70)),
                ("email", models.CharField(max_length=70)),
                ("dateInscription", models.DateField()),
            ],
        ),
    ]
