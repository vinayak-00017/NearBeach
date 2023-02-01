# Generated by Django 4.1.4 on 2023-02-01 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("NearBeach", "0002_initialise_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="kanbancolumn",
            name="kanban_property",
            field=models.CharField(
                choices=[
                    ("Normal", "Normal"),
                    ("Blocked", "Blocked"),
                    ("Closed", "Closed"),
                ],
                default="Normal",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="changetask",
            name="change_task_status",
            field=models.IntegerField(
                choices=[
                    (1, "Draft"),
                    (2, "Waiting for approval"),
                    (3, "Approved"),
                    (4, "Started"),
                    (5, "Finished"),
                    (6, "Rejected"),
                    (7, "Paused"),
                    (8, "Ready for QA"),
                ]
            ),
        ),
    ]
