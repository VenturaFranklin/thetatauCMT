# Generated by Django 2.2.3 on 2019-11-11 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0020_auto_20191110_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledge',
            name='explain_crime',
            field=models.TextField(blank=True, verbose_name='If yes, please explain.'),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='explain_expelled_college',
            field=models.TextField(blank=True, verbose_name='If yes, please explain.'),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='explain_expelled_org',
            field=models.TextField(blank=True, verbose_name='If yes, please explain.'),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='other_college',
            field=models.CharField(blank=True, max_length=60, verbose_name='Which? (Other college(s))'),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='other_frat',
            field=models.CharField(blank=True, help_text='Other than Theta Tau -- If no other, leave blank', max_length=60, verbose_name='Of which fraternities are you a member?'),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='other_tech',
            field=models.CharField(blank=True, help_text='If none, leave blank', max_length=60, verbose_name='Of which technical societies are you a member?'),
        ),
    ]
