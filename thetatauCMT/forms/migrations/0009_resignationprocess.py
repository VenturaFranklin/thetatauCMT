# Generated by Django 2.2.12 on 2020-08-02 23:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import forms.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("viewflow", "0008_jsonfield_and_artifact"),
        ("forms", "0008_collectionreferral"),
    ]

    operations = [
        migrations.CreateModel(
            name="ResignationProcess",
            fields=[
                (
                    "process_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="viewflow.Process",
                    ),
                ),
                (
                    "letter",
                    models.FileField(
                        upload_to=forms.models.get_resign_upload_path,
                        verbose_name="Resignation Letter",
                    ),
                ),
                (
                    "resign",
                    models.BooleanField(
                        choices=[(True, "Yes"), (False, "No")],
                        default=False,
                        verbose_name="For reasons which I deem good and sufficient, I wish to resign as a member of Theta Tau Fraternity.",
                    ),
                ),
                (
                    "secrets",
                    models.BooleanField(
                        choices=[(True, "Yes"), (False, "No")],
                        default=False,
                        verbose_name="I recognize that I am under a solemn obligation never to reveal any of the Secrets of the Fraternity, and I reaffirm my previous obligation never to reveal any secrets of Theta Tau Fraternity.",
                    ),
                ),
                (
                    "expel",
                    models.BooleanField(
                        choices=[(True, "Yes"), (False, "No")],
                        default=False,
                        verbose_name="I understand that I will be treated as an expelled member of Theta Tau and can only rejoin the fraternity by special petition to the Grand Regent.",
                    ),
                ),
                (
                    "return_evidence",
                    models.BooleanField(
                        choices=[(True, "Yes"), (False, "No")],
                        default=False,
                        verbose_name="I have or will returned all evidence of my membership in Theta Tau and all insignia previously possessed by me and now in my possession, and certify that evidence and insignia not returned to the chapter herewith has been lost or misplaced and if hereafter located will be returned.",
                    ),
                ),
                (
                    "obligation",
                    models.BooleanField(
                        choices=[(True, "Yes"), (False, "No")],
                        default=False,
                        verbose_name="I consent to the retention by my chapter and by Theta Tau Fraternity of all fees and dues heretofore paid by me while a member of said chapter and said Fraternity hereby releasing them from any and all obligations to me henceforth and forever.",
                    ),
                ),
                (
                    "fee",
                    models.BooleanField(
                        choices=[(True, "Yes"), (False, "No")],
                        default=False,
                        verbose_name="I have or will submit the $100 Resignation Processing Fee to the chapter.",
                    ),
                ),
                (
                    "signature",
                    models.CharField(
                        help_text="Please sign using your proper/legal name",
                        max_length=255,
                    ),
                ),
                (
                    "good_standing",
                    models.BooleanField(
                        choices=[(True, "Yes"), (False, "No")],
                        default=False,
                        verbose_name="The member is in good standing of Theta Tau.",
                    ),
                ),
                (
                    "returned",
                    models.BooleanField(
                        choices=[(True, "Yes"), (False, "No")],
                        default=False,
                        verbose_name="Did the member return all evidence of membership in Theta Tau?",
                    ),
                ),
                (
                    "financial",
                    models.BooleanField(
                        default=False,
                        verbose_name="Member has no current financial obligation to the chapter.",
                    ),
                ),
                (
                    "fee_paid",
                    models.BooleanField(
                        default=False,
                        verbose_name="Member submitted the $100 Resignation Processing Fee to the chapter.",
                    ),
                ),
                (
                    "signature_o1",
                    models.CharField(
                        help_text="Please sign using your proper/legal name",
                        max_length=255,
                    ),
                ),
                (
                    "signature_o2",
                    models.CharField(
                        help_text="Please sign using your proper/legal name",
                        max_length=255,
                    ),
                ),
                (
                    "approved_o1",
                    models.BooleanField(
                        choices=[(True, "Yes"), (False, "No")],
                        default=False,
                        verbose_name="Officer Approved",
                    ),
                ),
                (
                    "approved_o2",
                    models.BooleanField(
                        choices=[(True, "Yes"), (False, "No")],
                        default=False,
                        verbose_name="Officer Approved",
                    ),
                ),
                (
                    "officer1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="resign_off1",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Officer Signature",
                    ),
                ),
                (
                    "officer2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="resign_off2",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Officer Signature",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="resignation",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"abstract": False,},
            bases=("viewflow.process",),
        ),
    ]
