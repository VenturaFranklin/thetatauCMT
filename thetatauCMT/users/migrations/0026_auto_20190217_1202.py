# Generated by Django 2.0.3 on 2019-02-17 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20190113_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrolechange',
            name='role',
            field=models.CharField(choices=[('adviser', 'Adviser'), ('board member', 'Board Member'), ('committee chair', 'Committee Chair'), ('corresponding secretary', 'Corresponding Secretary'), ('employer/ee', 'Employer/Ee'), ('events chair', 'Events Chair'), ('faculty adviser', 'Faculty Adviser'), ('fundraising chair', 'Fundraising Chair'), ('house corporation president', 'House Corporation President'), ('house corporation treasurer', 'House Corporation Treasurer'), ('housing chair', 'Housing Chair'), ('other appointee', 'Other Appointee'), ('parent', 'Parent'), ('pd chair', 'Pd Chair'), ('pledge/new member educator', 'Pledge/New Member Educator'), ('project chair', 'Project Chair'), ('recruitment chair', 'Recruitment Chair'), ('regent', 'Regent'), ('risk management chair', 'Risk Management Chair'), ('rube goldberg chair', 'Rube Goldberg Chair'), ('scholarship chair', 'Scholarship Chair'), ('scribe', 'Scribe'), ('service chair', 'Service Chair'), ('social/brotherhood chair', 'Social/Brotherhood Chair'), ('treasurer', 'Treasurer'), ('vice regent', 'Vice Regent'), ('website/social media chair', 'Website/Social Media Chair')], max_length=50),
        ),
    ]