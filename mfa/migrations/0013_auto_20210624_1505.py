# Generated by Django 2.2 on 2021-06-24 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mfa", "0012_rename_user_keys_userkey"),
    ]

    operations = [
        migrations.CreateModel(
            name="OTPTracker",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("actor", models.CharField(max_length=50)),
                ("value", models.CharField(max_length=6)),
                ("success", models.BooleanField(blank=True)),
                ("done_on", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddIndex(
            model_name="otptracker",
            index=models.Index(fields=["actor"], name="mfa_otptrac_usernam_1f423f_idx"),
        ),
    ]